import socket
import sys
import time

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation error: " + str(msg))

def socket_bind():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s.bind((host, port))
        print("Listening on : " + str(port))
        s.listen(5)
        while True:
            conn, address = s.accept()
            print("Connection established to : " + address[0] + " at " + str(address[1]))
            conn.close()
    except socket.error as msg:
        print("Socket Bind Error: " + str(msg) + "\n")
        print("Restarting...\n")
        time.sleep(5)
        socket_bind()

def main():
    socket_create()
    socket_bind()

main()
