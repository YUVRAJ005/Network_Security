import socket,os,sys
from rsa import *

HOST = "127.0.0.1"
PORT = 5000

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {HOST}:{PORT} ...")    
    s.connect((HOST, PORT))
    print(f"Connected to {HOST} successfully\n") 

    filename = "File.txt"

    print("Receiving encryption keys...")
    received = s.recv(BUFFER_SIZE).decode()
    n , e = received.split(SEPARATOR)
    pub = (int(n),int(e))
    print("Encryption keys received successfully\n")
    with open(os.path.join(sys.path[0], filename), "r") as f:
        m = f.read()
    en = rsa_encrypt_text(pub,m)
    print(f"Encrypting and sending file \"{filename}\" ...\n")
    s.sendall(f"{filename}{SEPARATOR}{en}".encode())

print("__File Successfully encrypted and sent__\nConnection closed\n")


