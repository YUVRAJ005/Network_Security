import socket,os,sys
from elgamal import *

HOST = "127.0.0.1"
PORT = 5000

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {HOST}:{PORT} ...")    
    s.connect((HOST, PORT))
    print(f"Connected to {HOST} successfully") 

    print("Receiving encryption public key...")
    received = s.recv(BUFFER_SIZE).decode()
    e1,e2,p = received.split(SEPARATOR)
    e1,e2,p = int(e1),int(e2),int(p)
    print("Public key received successfully\n")

    filename = "File.txt"
    with open(os.path.join(sys.path[0], filename), "r") as f:
        m = f.read()

    print("Encrypting File...")
    en = encrypt_str_elgamal(m,e1,e2,p)
    print(f"Sending file : \"{filename}\" ...\n")
    s.sendall(f"{filename}{SEPARATOR}{en}".encode())

print("__File Successfully encrypted and sent__\nConnection closed\n")


