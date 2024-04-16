#!/usr/bin/env python

import os
os.system("apt-get install nikto")
os.system("clear")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VULNERABILITY ANALYSIS TOOL")

print("""
WELCOME TO VULNERABILITY ANALYSIS TOOL :)

""")

targetip = input("enter the ip: ")
os.system("nikto -h " + targetip)
