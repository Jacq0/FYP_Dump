import socket
from threading import Thread
import sys

serverIP = '192.168.1.2'
serverPORT = 65432

#set up for socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client method
def client():
    try:
        sock.connect((serverIP, serverPORT))
        thread.start()

        while True:
            msg = input()
            sock.sendall(msg.encode())
            
    except Exception as e:
        print("Error with Socket Connection... Exiting Program: " + str(e)) #drop out of client script and show error
        sys.exit()

#receive message thread to receive from server
def receive_command(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                print("Error: No Message")
            else:
                print(msg)
        except Exception as e:
            print("Error with Thread... Exiting Program: " + str(e)) #drop out of client script on error
            sys.exit()

#configure thread for recieve command
thread = Thread(target=receive_command, args=(sock))
thread.setDaemon(True) #set thread as daemon process, helps close up when program crashes.

if __name__ == '__main__':
    client()