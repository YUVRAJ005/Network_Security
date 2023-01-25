# CLIENT - ECC based encryption and decryption
import socket
from ecc import *
import pickle ,os,sys

HOST = "127.0.0.1"
PORT = 5000

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {HOST}:{PORT} ...")    
    s.connect((HOST, PORT))
    print(f"Connected to {HOST} successfully\n") 
    
    print("Receiving Encryption Public Key...")
    epub = s.recv(BUFFER_SIZE)
    epub = pickle.loads(epub)
    print("Public key received successfully\n")

    filename  = "File.txt"
    with open(os.path.join(sys.path[0], filename), "r") as f:
        content = f.read()
    
    print("Encrypting File...")
    encrypted = encrypt_ECC(content.encode(),epub)

    print("Sending File...")
    s.sendall(filename.encode())
    s.sendall(pickle.dumps(encrypted))

print("__File Successfully encrypted and sent__\nConnection closed\n")
   