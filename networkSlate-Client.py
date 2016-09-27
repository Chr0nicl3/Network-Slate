#!/usr/bin/env python

import socket
import sys
import threading
from Tkinter import *
from ScrolledText import *
import pickle

class client():
    def __init__(self):
        self.host = raw_input("Host IP : ")
        self.port = 3033
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        
        self.count = 0

    def recieveMessage(self):
        while True:
            received = self.socket.recv(1024)
            if received:
                temp = pickle.loads(received)
                self.num = temp[1]
                if temp[0]=='cast':
                    self.buf = temp[2]
                    self.cast()
                elif temp[0]=='backSpace':
                    self.backSpace()
                elif temp[0]=='delete':
                    self.delete()
                elif temp[0]=='reposition':
                    self.reposition()

                print temp
    
    def runEditor(self):
        self.root = Tk(className = "Network Slate - Client")
        self.textPadClient = ScrolledText(self.root, height=20, width=80)
        self.textPadClient.pack()
        self.root.mainloop()

    def cast(self):
        self.textPadClient.insert(self.num, self.buf)
        self.count = 0
    
    def reposition(self):
        self.textPadClient.mark_set(INSERT,self.num)
        self.count = 0  

    def backSpace(self):
        integer, decimal = self.num.split('.')
        if int(integer) == 1 and int(decimal)==0 and self.count == 0:
            self.textPadClient.delete(self.num)
            self.count += 1

        elif self.count ==1 and int(integer) ==1 and int(decimal) ==0:
            return

        else:
            print "else"
            self.textPadClient.delete(self.num)

    def delete(self):
        self.textPadClient.delete(self.num)

if __name__ == '__main__':
    Client = client()
    receiveThread = threading.Thread(target = Client.recieveMessage)
    receiveThread.start()

    editorThread = threading.Thread(target = Client.runEditor)
    editorThread.start()