#!/usr/bin/env python
# CreateVLan
# script to allocate static IP to virtual machines from guestConfig file and creating switches and invoking Guest
# Author Saurabh kukade, Ajay Shinde, Harshal Chaudhari

import os
import sys
import subprocess
import commands 
import ConfigParser


def executeCmd(cmd):
	print cmd
 	subprocess.call(cmd,shell=True)

def executeScripts(script):
	print script
	os.system("python "+script) 

if ((sys.argv[1]=='--create')or(sys.argv[1]=='-c')):
	scripts = []
	scripts.append("create-bridge.py")
	scripts.append("ipAddrAlloc.py")
	scripts.append("invokeGuests.py")
	for script in scripts:
		executeScripts(script)

elif ((sys.argv[1]=='-d')or(sys.argv[1]=='--destry')):
	scripts = []
	scripts.append("delete-bridge.py")
	for script in scripts:
		executeScripts(script)
else:
	executeCmd("echo -e 'usage: ./createVLan.py <argv> \n \t<argv> : -c || --create := Create VLan \n \t<argv> : -d || --delete := Delete VLan' ")


