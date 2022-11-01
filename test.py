import os
import sys
import json
import requests 
import urllib 

##amass
#val = input("Fill the domain: ")
#print("[*] Start amass...")
#os.system(f"amass enum -d {val} -o subdomain.txt")
#print("[*] Success...")

##nmap
fsubdomain = open('subdomain-test.txt','r') #subdomain.txt
line = fsubdomain.readline()

while line != "":
    #####
    print(line)
    #print(f"nmap {line} | grep \'open\' | awk -F / '{{print $1}}'")
    #openPort = os.system(f"nmap {line} | grep \'open\' | awk -F / '{{print $1}}'")
    openPort = os.system(f"nmap {line} | grep \'open\' | awk -F / \'{{print $1}}\'")
    print("OPEN PORT: " + str(openPort))
    print('[*] Scan done...')
    #####
    line = fsubdomain.readline()
fsubdomain.close()