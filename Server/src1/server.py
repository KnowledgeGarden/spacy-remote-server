# @see https://realpython.com/python-sockets/
 
import socket
import json
import struct
import pickle
from spacyclient import Sclient
sclient = Sclient()

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8777        # Port to listen on (non-privileged ports are > 1023)

def receive_data(conn):
    data_size = struct.unpack('>I', conn.recv(4))[0]
    received_payload = b""
    reamining_payload_size = data_size
    while reamining_payload_size != 0:
        received_payload += conn.recv(reamining_payload_size)
        reamining_payload_size = data_size - len(received_payload)
    data = json.loads(received_payload)

    return data

def send_msg(conn, msg):
    print('R ', msg)

    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    conn.sendall(msg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # while True:
        data = receive_data(conn)
        print('D', data)
        if  data:
            result = sclient.process(data)
            send_msg(conn, json.dumps(result).encode("utf-8"))