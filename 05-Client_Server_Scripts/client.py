import cv2
import numpy as np
import socket
import threading
from djitellopy import Tello

drone = Tello()
drone.connect()
drone.streamon()

#connect to the server
server_address = ('192.168.1.2', 8888)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

#cap = cv2.VideoCapture('udp://@0.0.0.0:11111')
#cap = cv2.VideoCapture(0)

#video doesn't work
while True:
    
    #grab frame from cam
    #ret, frame = cap.read()
    frame = drone.get_frame_read().frame
    frame = cv2.resize(frame, (320,240))

    if not frame:
        print("Error with drone feed")
        break

    #convert frame to bytes
    frame_str = cv2.imencode('.jpg', frame)[1].tobytes()

    #send to server
    sock.sendall(frame_str)

    #wait for response
    data = sock.recv(1024)