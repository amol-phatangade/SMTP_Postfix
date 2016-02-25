#!/usr/bin/env python
import os
import sys
import subprocess
import ConfigParser
parser=ConfigParser.ConfigParser()
parser.read('guestConfig')
listSection=list(parser.sections())
runKVM=[]
for x in range (1,len(listSection)+1):
#for x in range (1,2):
	mac_addr = parser.get('guest_%d' % (x),'mac_addr',)
	ip_addr = parser.get('guest_%d' % (x),'ip_addr',)
	ram = parser.get('guest_%d' % (x),'ram',)
	imageFile = parser.get('guest_%d' % (x),'imageFile',)
	switch_no = parser.get('guest_%d' % (x),'switch',)
	subprocess.call("cp ovs-ifup /etc/ovs-ifup"+str(x),shell=True)
	subprocess.call("cp ovs-ifdown /etc/ovs-ifdown"+str(x),shell=True)
	subprocess.call("sed -i \"s/.*switch=.*/switch=\'"+switch_no+"\'/\" /etc/ovs-ifup"+str(x),shell=True)
	subprocess.call("sed -i \"s/.*switch=.*/switch=\'"+switch_no+"\'/\" /etc/ovs-ifdown"+str(x),shell=True)
	subprocess.call("chmod 755 /etc/ovs-ifup"+str(x),shell=True)
	subprocess.call("chmod 755 /etc/ovs-ifdown"+str(x),shell=True)
	tempString = "kvm -m "+ram+" -net nic,macaddr="+mac_addr+" -net tap,script=/etc/ovs-ifup"+str(x)+",downscript=/etc/ovs-ifup"+str(x)+" -drive file="+imageFile
        print tempString
	if (x==1):
		runKVM=tempString
	else:
		runKVM=runKVM +" | "+tempString
subprocess.call(runKVM,shell=True)
#sync;
