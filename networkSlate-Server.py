#!/usr/bin/env python

import socket
import sys
import threading
from Tkinter import *
from ScrolledText import *
import pickle


class server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.port = 3033
        self.host = ''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server.bind((self.host, self.port))
        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()

        self.server.listen(10)
        
        self.num = 1.0
        self.buf=''
        self.contents = ''
        self.count = 0
        self.operation = ''
        self.new = 0

        self.lock = threading.Semaphore(value=1)

    def run_thread(self, conn, addr):
        print('Client connected with ' + addr[0] + ':' + str(addr[1]))
        returnAddr = addr[0]
        while True:
            temp = ''
            self.lock.acquire()
            data = self.operation, self.num, self.buf
            if self.new == 1:
                print data
                temp = pickle.dumps(data)
                conn.sendall(temp) 
                self.new = 0
            self.lock.release()

    def runServer(self):
        print('Waiting for connections on port %s' % (self.port))
        conn, addr = self.server.accept()
        threading.Thread(target=self.run_thread, args=(conn, addr)).start()


    def runEditor(self):
        self.root = Tk(className = "Network Slate - Server")
        self.textPadServer = ScrolledText(self.root, height=20, width=80)
        self.textPadServer.pack()
        self.root.bind('<Key>', self.cast)
        self.root.bind('<BackSpace>', self.backSpace)
        self.root.bind('<Delete>', self.delete)
        self.root.bind('<Button-1>', self.reposition)
        self.root.bind('<Left>', self.reposition)
        self.root.bind('<Up>', self.reposition)
        self.root.bind('<Right>', self.reposition)
        self.root.bind('<Down>', self.reposition)

        """
        ignore the following keys
        """
        self.root.bind('<Shift_L>', lambda e: 'break')
        self.root.bind('<Control_L>', lambda e: 'break')
        self.root.bind('<Alt_L>', lambda e: 'break')
        self.root.bind('<Prior>', lambda e: 'break')
        self.root.bind('<Next>', lambda e: 'break')
        self.root.bind('<Home>', lambda e: 'break')
        self.root.bind('<End>', lambda e: 'break')
        self.root.bind('<Insert>', lambda e: 'break')
        self.root.bind('<F1>', lambda e: 'break')
        self.root.bind('<F2>', lambda e: 'break')
        self.root.bind('<F3>', lambda e: 'break')
        self.root.bind('<F4>', lambda e: 'break')
        self.root.bind('<F5>', lambda e: 'break')
        self.root.bind('<F6>', lambda e: 'break')
        self.root.bind('<F7>', lambda e: 'break')
        self.root.bind('<F8>', lambda e: 'break')
        self.root.bind('<F9>', lambda e: 'break')
        self.root.bind('<F1>', lambda e: 'break')
        self.root.bind('<F2>', lambda e: 'break')
        self.root.bind('<F3>', lambda e: 'break')
        self.root.bind('<F4>', lambda e: 'break')
        self.root.bind('<F5>', lambda e: 'break')
        self.root.bind('<F6>', lambda e: 'break')
        self.root.bind('<F7>', lambda e: 'break')
        self.root.bind('<F8>', lambda e: 'break')
        self.root.bind('<F9>', lambda e: 'break')
        self.root.bind('<F10>', lambda e: 'break')
        self.root.bind('<F11>', lambda e: 'break')
        self.root.bind('<F12>', lambda e: 'break')
        self.root.bind('<Alt-a>', lambda e: 'break')
        self.root.bind('<Alt-b>', lambda e: 'break')
        self.root.bind('<Alt-c>', lambda e: 'break')
        self.root.bind('<Alt-d>', lambda e: 'break')
        self.root.bind('<Alt-e>', lambda e: 'break')
        self.root.bind('<Alt-f>', lambda e: 'break')
        self.root.bind('<Alt-g>', lambda e: 'break')
        self.root.bind('<Alt-h>', lambda e: 'break')
        self.root.bind('<Alt-i>', lambda e: 'break')
        self.root.bind('<Alt-j>', lambda e: 'break')
        self.root.bind('<Alt-k>', lambda e: 'break')
        self.root.bind('<Alt-l>', lambda e: 'break')
        self.root.bind('<Alt-m>', lambda e: 'break')
        self.root.bind('<Alt-n>', lambda e: 'break')
        self.root.bind('<Alt-o>', lambda e: 'break')
        self.root.bind('<Alt-p>', lambda e: 'break')
        self.root.bind('<Alt-q>', lambda e: 'break')
        self.root.bind('<Alt-r>', lambda e: 'break')
        self.root.bind('<Alt-s>', lambda e: 'break')
        self.root.bind('<Alt-t>', lambda e: 'break')
        self.root.bind('<Alt-u>', lambda e: 'break')
        self.root.bind('<Alt-v>', lambda e: 'break')
        self.root.bind('<Alt-w>', lambda e: 'break')
        self.root.bind('<Alt-x>', lambda e: 'break')
        self.root.bind('<Alt-y>', lambda e: 'break')
        self.root.bind('<Alt-z>', lambda e: 'break')
        self.root.bind('<Shift-a>', lambda e: 'break')
        self.root.bind('<Shift-b>', lambda e: 'break')
        self.root.bind('<Shift-c>', lambda e: 'break')
        self.root.bind('<Shift-d>', lambda e: 'break')
        self.root.bind('<Shift-e>', lambda e: 'break')
        self.root.bind('<Shift-f>', lambda e: 'break')
        self.root.bind('<Shift-g>', lambda e: 'break')
        self.root.bind('<Shift-h>', lambda e: 'break')
        self.root.bind('<Shift-i>', lambda e: 'break')
        self.root.bind('<Shift-j>', lambda e: 'break')
        self.root.bind('<Shift-k>', lambda e: 'break')
        self.root.bind('<Shift-l>', lambda e: 'break')
        self.root.bind('<Shift-m>', lambda e: 'break')
        self.root.bind('<Shift-n>', lambda e: 'break')
        self.root.bind('<Shift-o>', lambda e: 'break')
        self.root.bind('<Shift-p>', lambda e: 'break')
        self.root.bind('<Shift-q>', lambda e: 'break')
        self.root.bind('<Shift-r>', lambda e: 'break')
        self.root.bind('<Shift-s>', lambda e: 'break')
        self.root.bind('<Shift-t>', lambda e: 'break')
        self.root.bind('<Shift-u>', lambda e: 'break')
        self.root.bind('<Shift-v>', lambda e: 'break')
        self.root.bind('<Shift-w>', lambda e: 'break')
        self.root.bind('<Shift-x>', lambda e: 'break')
        self.root.bind('<Shift-y>', lambda e: 'break')
        self.root.bind('<Shift-z>', lambda e: 'break')
        self.root.bind('<Control-a>', lambda e: 'break')
        self.root.bind('<Control-b>', lambda e: 'break')
        self.root.bind('<Control-c>', lambda e: 'break')
        self.root.bind('<Control-d>', lambda e: 'break')
        self.root.bind('<Control-e>', lambda e: 'break')
        self.root.bind('<Control-f>', lambda e: 'break')
        self.root.bind('<Control-g>', lambda e: 'break')
        self.root.bind('<Control-h>', lambda e: 'break')
        self.root.bind('<Control-i>', lambda e: 'break')
        self.root.bind('<Control-j>', lambda e: 'break')
        self.root.bind('<Control-k>', lambda e: 'break')
        self.root.bind('<Control-l>', lambda e: 'break')
        self.root.bind('<Control-m>', lambda e: 'break')
        self.root.bind('<Control-n>', lambda e: 'break')
        self.root.bind('<Control-o>', lambda e: 'break')
        self.root.bind('<Control-p>', lambda e: 'break')
        self.root.bind('<Control-q>', lambda e: 'break')
        self.root.bind('<Control-r>', lambda e: 'break')
        self.root.bind('<Control-s>', lambda e: 'break')
        self.root.bind('<Control-t>', lambda e: 'break')
        self.root.bind('<Control-u>', lambda e: 'break')
        self.root.bind('<Control-v>', lambda e: 'break')
        self.root.bind('<Control-w>', lambda e: 'break')
        self.root.bind('<Control-x>', lambda e: 'break')
        self.root.bind('<Control-y>', lambda e: 'break')
        self.root.bind('<Control-z>', lambda e: 'break')

        self.root.mainloop()

    def cast(self, key):
        self.lock.acquire()
        self.contents = self.textPadServer.get(self.num)
        self.num = self.textPadServer.index("insert")
        self.buf = self.contents
        self.operation = 'cast'
        print self.buf
        self.count = 0
        self.new = 1
        self.lock.release()
    
    def reposition(self, key):
        self.lock.acquire()
        self.num = self.textPadServer.index("insert")
        self.num = self.textPadServer.index("insert")
        self.num = self.textPadServer.index("insert")
        self.num = self.textPadServer.index("insert")
        self.operation = 'reposition'
        self.count = 0  
        self.new = 1
        self.lock.release()

    def backSpace(self, key):
        self.lock.acquire()
        self.num = self.textPadServer.index("insert")
        self.num = self.textPadServer.index("insert")
        self.num = self.textPadServer.index("insert")
        self.num = self.textPadServer.index("insert")
        self.operation = 'backSpace'
        integer, decimal = self.num.split('.')
        print integer,'.',decimal
        self.new = 1
        if int(integer) == 1 and int(decimal)==0 and self.count == 0:
            self.count += 1

        elif self.count ==1 and int(integer) ==1 and int(decimal) ==0:
            return
        else:
            print "else"
        self.lock.release()

    def delete(self, key):
        self.lock.acquire()
        self.num = self.textPadServer.index('insert')
        self.operation = 'delete'
        self.new = 1
        self.lock.release()


if __name__ == '__main__':
    Server = server()
    serverThread = threading.Thread(target = Server.runServer)
    serverThread.start()

    editorThread = threading.Thread(target = Server.runEditor)
    editorThread.start()

