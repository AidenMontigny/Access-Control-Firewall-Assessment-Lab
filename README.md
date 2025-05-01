<h1> Access Control Firewall Assessment Lab </h1>

<h2>Description</h2>
This project demonstrates the configuration and assessment of firewall rules using pfSense within a hybrid network environment. The lab involved implementing access control policies to restrict specific traffic types—such as gaming ports, ICMP, social media, and streaming services—and validating the rules using tools like Nmap and Greenbone Vulnerability Manager (GVM). Key outcomes include reinforcing secure port management, enforcing encrypted communication (HTTPS), and applying domain blocking for enhanced policy control. The project highlights practical network security implementation and vulnerability mitigation in real-world scenarios.
<br />

<h2>Utilities Used</h2>

- <b> pfSense </b> 
- <b> Greenbone </b>
- <b> Nmap </b>

<h2>Environments Used </h2>

- <b> Windows Server 2022 </b>

<h2>Project walk-through:</h2>

<p align="left">
The HTTPS port is configured with the value '8443'. <br/><br/>
  <img src="Screenshot 2025-04-30 214420.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The pfSense URL is configured to end with port 8443. <br/><br/>
  <img src="Screenshot 2025-04-30 214428.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The Traffic Graph has been successfully integrated into the dashboard for real-time network  <br/> traffic monitoring. <br/><br/>
  <img src="Screenshot 2025-04-30 214437.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The ports associated with World of Warcraft (6881-6999) have been successfully blocked to  <br/> restrict access and enhance network security. <br/><br/>
  <img src="Screenshot 2025-04-30 214444.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The ICMP protocol has been successfully blocked on the pfSense firewall to prevent potential  <br/> network reconnaissance and mitigate DDoS attack risks. <br/><br/>
  <img src="Screenshot 2025-04-30 214452.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The firewall configuration successfully blocks access to two social media websites, enhancing  <br/> network security by restricting non-essential web traffic. <br/><br/>
  <img src="Screenshot 2025-04-30 214459.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The firewall configuration has disabled access to specific domains, preventing any communication  <br/> or  data exchange with those sites for enhanced security. <br/><br/>
  <img src="Screenshot 2025-04-30 214508.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
Access to two streaming media websites has been blocked, ensuring that network resources are <br/> protected from potentially unauthorized or high-bandwidth traffic. <br/><br/>
  <img src="Screenshot 2025-04-30 214515.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The domains have been disabled to prevent access to specific websites, enhancing network security <br/> by  restricting unwanted or potentially harmful traffic. <br/><br/>
  <img src="Screenshot 2025-04-30 214524.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The Nmap command is executed on the pfSense firewall's IP address to perform a network scan, <br/> identifying open ports and assessing the firewall's security posture. <br/><br/>
  <img src="Screenshot 2025-04-30 214532.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
<p align="left">
The GVM scan report provides detailed findings from a vulnerability assessment, highlighting  <br/> potential security weaknesses and areas for improvement in the system’s configuration. <br/><br/>
  <img src="Screenshot 2025-04-30 214541.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
  <br/>
