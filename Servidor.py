#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq
import time


context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket

p = "tcp://127.0.0.1:50007" # how and where to communicate
s.bind(p) # bind socket to the address
	
while True:
	a = input("digite a lista => att,1:1;1:3\n")
	msg = str("4 " + a)
	s.send(msg.encode())


