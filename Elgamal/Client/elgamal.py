import Crypto.Util.number as number

#Inverse of A in mod M
def modular_inverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

#Key generation 
def elgamal_key_generate(bits):
    p = number.getPrime(bits-1)
    while True:
        e1 = number.getRandomRange(3, p+1) 
        #check if (e1^i != 1 mod p) for 0 < i < p-1
        for i in range(1, p-1):
            if (pow(e1, i, p) == 1):
                break
        break
    #private key
    d = number.getRandomRange(2, p-1)
  
    #public key
    e2 = pow(e1, d, p)
    return e1,e2,p,d

# g=e1
# y=e2
# x=d

#encryption
def encrypt_elgamal(e1, e2, p, m):
    r = number.getRandomRange(2, p-1)
    #cipher text
    c1 = pow(e1, r, p)
    c2 = (m * pow(e2, r, p)) % p
    #return(c1,c2)
    return f"{c1} {c2} "

#decryption
def decrypt_elgamal(c1, c2, d, p):
    #message
    m = (c2 * pow(c1, p-1-d, p)) % p
    return m

def encrypt_str_elgamal(plaintext,e1,e2,p):
    encrypted = ""
    for letter in plaintext:
       #print(ord(letter))
       encrypted = encrypted + encrypt_elgamal(e1,e2,p,ord(letter))
    return encrypted

def decrypt_str_elgamal(cipher,d,p):
    temp = cipher.split(" ")
    l = len(temp)
    plaintext = ""
    for i in range(0,l-1,2):
        #print(temp[i],type(temp[i]))
        c1 = int(temp[i])
        print(c1)
        c2 = int(temp[i+1])
        print(c2)
        #print(chr(decrypt_elgamal(c1,c2,d,p)))
        plaintext = plaintext + chr(decrypt_elgamal(c1,c2,d,p))

    return plaintext

# e1,e2,p,d = elgamal_key_generate(14)
# s = "YY\nY\n"
# e = encrypt_str_elgamal(s,e1,e2,p)
# print(e+"\n")
# dr = decrypt_str_elgamal(e,d,p)
# print(dr)


# e1,e2,p,d = elgamal_key_generate(14)
# x = encrypt_elgamal(e1,e2,p,89)
# print(x)

# m = decrypt_elgamal(c1,c2,d,p)
# print(m)
# print(e1)
# print(e2)
# print(p)
# print(d)
# print(c1)
# print(c2)
# print(m)