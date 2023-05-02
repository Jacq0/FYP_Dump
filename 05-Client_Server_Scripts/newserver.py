import socket
import threading

#server IP and port
IP = '192.168.1.2'
PORT = 65432

#store connected clients
clients = {}

#handle client connections
def handle_client(conn, addr, client_id):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Received from {client_id}: {data.decode()}')
    
    #delete client if no data received
    del clients[client_id]
    conn.close()
    print(f'{addr} disconnected')

#send message to specified client, ID is their port, which is unique
def send_message(client_id, message):
    if client_id in clients:
        conn = clients[client_id][0]
        conn.sendall(message.encode())
    else:
        print(f'Client {client_id} not found')

#send all connected clients a message
def send_all_message(message):
    for c in clients:
        conn = clients[c][0]
        conn.sendall(message.encode())

#run a message thread seperately so it never gets interruped by connections
def message_thread():
    while True:
        message = input('Enter message to send: ')
        send_all_message(message)

#start up server, run messaging thread and client handler thread
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #set up socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((IP, PORT))
        s.listen()
        print(f'Listening on {IP}:{PORT}')

        #messaging thread
        threading.Thread(target=message_thread).start()

        #loop for listening to clients
        while True:
            conn, addr = s.accept()
            client_id = addr[1]
            clients[client_id] = (conn, addr)
            print(f'{addr} connected')

            #client handler thread
            threading.Thread(target=handle_client, args=(conn, addr, client_id)).start()
            
            #send a message to the new client 
            msg = f'Hello {client_id}!'
            send_message(client_id, msg)

if __name__ == '__main__':
    start_server()