#!us/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input("Enter the ip to scan: ")
port = int(input("Enter port to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is Closed.")
    else:
        print("The Port is Open")

portScanner(port)