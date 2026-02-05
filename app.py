from __future__ import annotations

import os
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path
from flask import Flask, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "scans.db"

NMAP_PATH = os.getenv("NMAP_PATH", "nmap")
CLAMAV_PATH = os.getenv("CLAMAV_PATH", "clamscan")

app = Flask(__name__)


def get_db() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_db() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_type TEXT NOT NULL,
                target TEXT NOT NULL,
                status TEXT NOT NULL,
                output TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )


def record_scan(scan_type: str, target: str, status: str, output: str) -> None:
    with get_db() as connection:
        connection.execute(
            """
            INSERT INTO scans (scan_type, target, status, output, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (scan_type, target, status, output, datetime.utcnow().isoformat(timespec="seconds")),
        )


def run_command(command: list[str]) -> tuple[str, str]:
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return (
            "missing",
            "Required scanner binary was not found. Install it or configure the path.",
        )

    status = "success" if result.returncode == 0 else "warning"
    output = (result.stdout + "\n" + result.stderr).strip()
    if not output:
        output = "No output returned by the scanner."
    return status, output


def validate_target(target: str) -> str:
    target = target.strip()
    if not target:
        raise ValueError("Target cannot be empty.")
    return target


def validate_path(target: str) -> str:
    path = Path(target).expanduser().resolve()
    if not path.exists():
        raise ValueError("Target path does not exist.")
    return str(path)


@app.route("/")
def index() -> str:
    with get_db() as connection:
        scans = connection.execute(
            "SELECT id, scan_type, target, status, created_at FROM scans ORDER BY id DESC LIMIT 6"
        ).fetchall()
    return render_template("index.html", scans=scans)


@app.route("/admin")
def admin() -> str:
    with get_db() as connection:
        scans = connection.execute(
            "SELECT id, scan_type, target, status, output, created_at FROM scans ORDER BY id DESC"
        ).fetchall()
    return render_template("admin.html", scans=scans)


@app.route("/scan/nmap", methods=["POST"])
def scan_nmap() -> str:
    target = request.form.get("target", "")
    try:
        target = validate_target(target)
        status, output = run_command([NMAP_PATH, "-sV", "-T4", target])
    except ValueError as exc:
        status = "error"
        output = str(exc)

    record_scan("intrusion", target, status, output)
    return redirect(url_for("admin"))


@app.route("/scan/clamav", methods=["POST"])
def scan_clamav() -> str:
    target = request.form.get("path", "")
    try:
        target = validate_path(target)
        status, output = run_command([CLAMAV_PATH, "-r", "-i", target])
    except ValueError as exc:
        status = "error"
        output = str(exc)

    record_scan("malware", target, status, output)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
