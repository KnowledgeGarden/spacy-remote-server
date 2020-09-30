# @see https://realpython.com/python-sockets/
# @see https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data

import socket
import json
import struct

from collections import OrderedDict

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8777        # The port used by the server
# text = 'co2 causes climate change'
# text = """The pandemic of obesity, type 2 diabetes mellitus (T2DM) and nonalcoholic fatty liver disease (NAFLD) has frequently been associated with dietary intake of saturated fats (1) and specifically with dietary palm oil (PO) (2)."""
# text = """The molecular weight of single-stranded DNA from the slime mold Physarum polycephalum has been determined by alkaline gradient centrifugation. """

# text = """On the basis of a chromosome number of 50 per nucleus and a DNA content of 1 μμg per nucleus, we are led to conclude that at pH 12 each chromosome dissociates into 300 (single-stranded) pieces of DNA """
text = """ Certain genes that help cells grow and divide or make them live longer than they should are called oncogenes."""
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

data = OrderedDict([
        ("cmd", 'foo'),
        ("text", text)
])

textStr = json.dumps(data)
print(textStr)
textBytes = str.encode(textStr)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send_msg(s, textBytes)
    data = recv_msg(s)
print(data)
jsonStr = json.loads(data.decode('utf-8'))
print('Received', repr(jsonStr))