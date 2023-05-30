# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:25:09 2023

@author: mohamed saeed
"""

from socket import *
s=socket(AF_INET,SOCK_STREAM)
host = "127.0.0.1"
port = 7002
s.connect((host,port))
print("successfully connected!")

while True:
    client_data=input("client: ")
    s.send(client_data.encode("utf=8"))
    if client_data == "Q":
        break
    
    server_data=s.recv(2048)
    print("server: ",server_data.decode("utf=8"))
    if server_data.decode("utf=8") == "Q":
        break
    
s.close()    
    
