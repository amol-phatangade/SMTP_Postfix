#!/usr/bin/env python
# script to allocate static IP to virtual machines from guestConfig file
#Author Saurabh kukade
import os
import sys
import subprocess
import commands 
import ConfigParser

parser=ConfigParser.ConfigParser()
parser.read('guestConfig')
listSection=list(parser.sections())
workingDir=subprocess.check_output("pwd",shell=True)
workingDir=((workingDir).splitlines())[0]

#Fucntion to allocate static IP Addr to virtual machine

def ipAlloc(ipAddr,netmask,imageFile):

#mounting file system of qemu image
	print "Mounting file system of "+imageFile
	offsetVal=(int (commands.getoutput("fdisk -l "+imageFile+" | grep \Linux | grep \* | awk '{print $3}'")))*512
	subprocess.call("mount -o loop,offset="+str(offsetVal)+" "+imageFile+" /mnt",shell=True)
#changing interface file and allocating static IP
	print "Allocating static ip "+ipAddr+" in file /mnt/etc/network/interfaces of "+imageFile
	os.chdir('/mnt/etc/network/')
	fo1= open('interfaces.bak','a+')
	content=fo1.read()
	fo1.close()
	fo1= open('interfaces','w+')
	fo1.write(content+"\n#static ip allocation\nauto eth0\niface eth0 inet static\naddress "+ipAddr+"\nnetmask "+netmask+"\n");
	fo1.close()
	subprocess.call("cd ",shell=True)
	print "Done Allocating IP adress to machine"
	subprocess.call("sync",shell=True)
	subprocess.call("sleep 2s",shell=True)
	os.chdir(workingDir)
#unmounting and deleting device and machine
	print "Unmounting file system "
	subprocess.call("umount /mnt",shell=True)
	return;

listGuest=parser.sections()
for guest in listGuest:
	print "\n"
	mac_addr = parser.get(guest,'mac_addr',)
	ip_addr = parser.get(guest,'ip_addr',)
	ram = parser.get(guest,'ram',)
	imageFile = parser.get(guest,'imageFile',)
	netmask=parser.get(guest,'netmask',)
	ipAlloc(ip_addr,netmask,imageFile)
	print "Done for Machine "+guest+"\n" 
