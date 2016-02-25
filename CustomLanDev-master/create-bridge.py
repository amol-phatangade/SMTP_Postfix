#! /usr/bin/python

# Script to Create and Connect Bridges from SwitchConfig file
# Author Ajay Shinde

import subprocess, sys, ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("switchconf")
def shortdelay():
 subprocess.call("sleep 1",shell=True)

def executeCmd(cmd):
 print cmd
 subprocess.call(cmd,shell=True)
 shortdelay()

cnt = len(list(Config.sections()))
switch_name = Config.get('switch_0','switch_name')
port = Config.get('switch_0','port')
ip = Config.get('switch_0','ip')
print "creating switches"

cmds = []

cmds.append("ifconfig eth0 0 >> /dev/null 2>&1");
cmds.append("service networking stop >> /dev/null 2>&1"); 
cmds.append("service networking start >> /dev/null 2>&1");
cmds.append("ovs-vsctl add-br "+switch_name);
cmds.append("ovs-vsctl add-port "+switch_name+" "+port);
cmds.append("ifconfig "+switch_name+" "+ip+" up");
cmds.append("service openvswitch-switch restart >> /dev/null 2>&1"); 
	
for x in xrange(1, cnt):
   switch_name=Config.get("switch_"+str(x),'switch_name')
   cmds.append("ovs-vsctl add-br "+switch_name);
   cmds.append("ifconfig "+switch_name+" up"); 

for x in xrange(2,cnt):
   switch_name=Config.get("switch_"+str(x),'switch_name')	
   fst_switch = Config.get("switch_"+str(x),'fst_switch')
   snd_switch = Config.get("switch_"+str(x),'snd_switch')
   port1 = Config.get("switch_"+str(x),'port1')
   port2 = Config.get("switch_"+str(x),'port2')
	
   cmds.append("ovs-vsctl --may-exist add-port "+fst_switch+" "+port1+" -- set Interface "+port1+" type=patch options:peer="+port2);
   cmds.append("ovs-vsctl --may-exist add-port "+snd_switch+" "+port2+" -- set Interface "+port2+" type=patch options:peer="+port1);
   cmds.append("ifconfig "+switch_name+" up");

for cmd in cmds:
  executeCmd(cmd)

print cnt, "switch created Sucessfully "
print cnt, "Peer done by patch cable "
sys.exit(0)
