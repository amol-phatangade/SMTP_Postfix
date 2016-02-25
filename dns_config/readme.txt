1) install bind9.
   sudo apt-get install bind9 bind9utils bind9-doc
2) change /etc/default/bind9
   after change /etc/default/bind9 looklike this:
   	 OPTIONS="-4 -u bind"

3) change /etc/bind/named.conf.options
   for more detile see curcunt derectory named.conf.options

4) change /etc/bind/named.conf.local
   for more detile see curcunt derectory named.conf.local

5) create forword zone (mkdir /etc/bind/zones)

6) copy /etc/bind/db.local and /etc/bind/db.127 to /etc/bind/zones folder
   sudo cp /etc/bind/db.local  /etc/bind/zones/db.$our_domailnem.com
   for more detaile see curcunt directory zones directory.

7) check BIND configuration syntax.
   Run the following command to check the syntax of the named.conf* files:
   sudo named-checkconf 

8) The named-checkzone command can be used to check the correctness of your zone files. Its first argument specifies a zone name, and the second argument specifies the corresponding zone file, which are both defined in named.conf.local.
   For example, to check the "nyc3.example.com" forward zone configuration, run the following command (change the names to match your forward zone and file):

       sudo named-checkzone nyc3.example.com db.nyc3.example.com

   And to check the "128.10.in-addr.arpa" reverse zone configuration, run the following command (change the numbers to match your reverse zone and file):

       sudo named-checkzone 128.10.in-addr.arpa /etc/bind/zones/db.10.128

9) if there is no error then go to step 10 otherwise resolve they all errors and wornings and then go step 10. 

10) sudo service bind9 restart

11) edit /etc/resolvconf/resolv.conf.d/head
    add your name server name add ip for eg.
    search nyc3.example.com  # your private domain
    nameserver 10.128.10.11  # ns1 private IP address
    nameserver 10.128.20.12  # ns2 private IP address

12) resolvconf -u

13) see /etc/resolv.conf
