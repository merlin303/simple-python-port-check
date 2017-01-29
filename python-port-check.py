#!/usr/bin/python
#check if a port is open or closed
import socket
#import python library
ip = raw_input("Enter an IP Address: ")
port = input("Enter the Port Number:")
#sets the variables ip & port
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
#set the varibble for sock uses socket library
if sock.connect_ex ((ip,port)):
	print "Port", port, "is closed"
else:
	print "Port", port, "is open"

#set the if statement 
