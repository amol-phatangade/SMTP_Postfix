# CustomLanDev
We are building custom LAN with custom protocol and rules of communication.

<h1> Automation of small cluster to test protocols.</h1>
<p>To test and develop software or protocols on distributed
	computing, we need platform for it.<br> Platform where we
	can test and check for dry runs etc. <br>
</p>
<p>
	This small project is for automating custom cluster,
	custom in the sense IP addresses allocation,<br> creating a
	virtual swishes and automating a communication between 
	them using IP tables and virtual machines.<br>
	By taking all the parameters through config files. <br>
</p>
<ul>
	We have used: <br>
	<li>1. Python for scripting language.</li>
	<li>2. Qemeu for virtual machines in cluster. </li>
	<li>3. OpenVswitch for virtual switch.</li>
	<li>4. Debian wheezy for Operating system. (Guest) </li>
	<li>5. <a href https://en.wikipedia.org/wiki/Preseed> Preseeding </a>for installing operating system on guest(s). </li>
</ul>
<ul>
	We automated:
	<li>1. Invoking guest machines through script. </li>
	<li>2. Preparation of guest machine.</li>
	<li>2. Ip address allocation before starting guest system. </li>
	<li>3. Switches creation as well as deletion.</li>
	<li>4. Networking between guests and host as per given rules. </li>
</ul>

