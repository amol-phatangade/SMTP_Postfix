#! /usr/bin/python

# Script to Delete the Bridges from SwitchConfig file
# Author Ajay Shinde

import subprocess, sys, ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("guestConfig")

cnt=len(list(Config.sections()))

for x in xrange(1,cnt+1):
  switch_name = Config.get("guest_"+str(x), 'switch')
  subprocess.call("ovs-vsctl del-br "+switch_name,shell=True);

print cnt, "switches deleted successfully "
sys.exit(0)





 

