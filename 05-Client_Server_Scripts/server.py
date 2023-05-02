import cv2
import numpy as np
import socket
from threading import Thread

#max number of clients
num_clients = 5

sock = socket.socket()

host = '192.168.1.2'
port = 8888

sock.bind((host, port))

sock.listen(num_clients)

print('Waiting for Connection...')

def client_thread(conn, client_address):

    cv2.namedWindow(str(client_address[1]), cv2.WINDOW_NORMAL)

    #receive and display video frames
    while True:
        data = b''
        while True:
            #receive from client
            packet = conn.recv(4096)
            if not packet:
                break
            data += packet

            #break if we only receive a small bit of the frame
            if len(packet) < 4096:
                break

        #convert to frame
        buff = np.frombuffer(data, np.uint8)
        frame = cv2.imdecode(buff, cv2.IMREAD_COLOR)

        #show frame with cv2
        cv2.imshow(str(client_address[1]), frame)
        cv2.waitKey(1000)

        #respond to client
        conn.sendall('Received'.encode('utf-8'))

#loop to check connections and make threads for each.
while True:
    conn, client_address = sock.accept()
    print(f'Connection: {client_address}')

    thread = Thread(target=client_thread, args=(conn, client_address))
    thread.start()

