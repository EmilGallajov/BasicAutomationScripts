#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT SCANNING")
print("""
WELCOME TO PORT SCANNING:)

1)Basic scan
2)Sevice and Version data
3)OS data

""")
moveno = input("enter movement: ")

if(moveno == "1"):
    targetip = input("enter target ip: ")
    os.system("nmap " + targetip)
elif(moveno == "2"):
    targetip = input("enter target ip:")
    os.system("nmap -sS -sV " + targetip)
elif(moveno== "3"):
    targetip = input("enter target ip:")
    os.system("nmap -A " + targetip)

else: print("Error!")

