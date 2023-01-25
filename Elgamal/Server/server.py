import socket
import time
from elgamal import *
import os,sys

HOST = "127.0.0.1"
PORT = 5000 

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

print("Getting ready...\nGenerating public and private keys...")
time.sleep(1)
e1,e2,p,d = elgamal_key_generate(14)
print("Keys generated successfully...\nServer ready...\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening on port : ",PORT)
    conn, addr = s.accept()
    print(f"Connection request from {addr}")
    with conn:
        print(f"Connection established with {addr}\n")
        print("Sending public key...")
        conn.send(f"{e1}{SEPARATOR}{e2}{SEPARATOR}{p}".encode())
        print("Public key Sent successfully\n")

        print("Receiving file...\n")
        received = conn.recv(BUFFER_SIZE).decode()
        filename, bytes_read = received.split(SEPARATOR)

        print("Decrypting file...\n")
        pt = decrypt_str_elgamal(bytes_read,d,p)
        with open(os.path.join(sys.path[0], filename), "w") as f:
            f.write(pt)

print("__File Successfully decrypted and saved__\nConnection closed\n")
