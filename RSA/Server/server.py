import socket
import time,os,sys
from rsa import *

HOST = "127.0.0.1"
PORT = 5000 

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

print("Getting ready...\nGenerating public and private keys...")
time.sleep(1)
priv,pub = rsa_generate_key(13,17)
n = str(pub[0])
e = str(pub[1])
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
        conn.send(f"{n}{SEPARATOR}{e}".encode())
        print("Public key sent successfully\n")
        
        print("Receiving File...")
        received = conn.recv(BUFFER_SIZE).decode()
        filename, bytes_read = received.split(SEPARATOR)

        print("Decrypting File...\n")
        pt = rsa_decrypt_text(priv,bytes_read)

        with open(os.path.join(sys.path[0], filename), "w") as f:
            f.write(bytes_read)

print("__File Successfully decrypted and saved__\nConnection closed\n")
