# Server - ECC based encryption and decryption
from ecc import *
import socket
import time,os,sys
import pickle


HOST = "127.0.0.1"
PORT = 5000 

BUFFER_SIZE = 50000
SEPARATOR = "<SEPARATOR>"

print("Getting ready...\nGenerating public and private keys...")
time.sleep(1)
print("Keys generated successfully\nServer ready\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening on port : ",PORT)
    conn, addr = s.accept()
    print(f"Connection request from {addr}")
    with conn:
        print(f"Connection established with {addr}\n")
        
        print("Sending public key...")
        conn.send(pickle.dumps(pubKey))
        print("Public key Sent successfully\n")

        print("Receiving file...")
        filename = conn.recv(BUFFER_SIZE).decode()
        encrypted = conn.recv(BUFFER_SIZE)
        
        print("Decrypting file...\n")
        plainText = decrypt_ECC(pickle.loads(encrypted),privKey)
        plainText = plainText.decode()

        with open(os.path.join(sys.path[0], filename), "w") as f:
            f.write(plainText)
        
print("__File Successfully decrypted and saved__\nConnection closed\n")

