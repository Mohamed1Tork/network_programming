# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:16:53 2023

@author: mohamed saeed
"""
from socket import *
s= socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"
port=7002
s.bind((host,port))
s.listen(5)
client,add=s.accept()
print("connection from: ",add[0])

while True:
    received_data=client.recv(2048)
    print("client: ",received_data.decode("utf=8"))
    if received_data.decode("utf=8") == "Q":
        break
    
    send_data=input("server: ")
    client.send(send_data.encode("utf=8"))
    if send_data == "Q":
        break
    
    
s.close()
