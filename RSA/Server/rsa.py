import math, random

def modular_inverse(A, M):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def rsa_generate_key(p, q):
    n = p * q

    # Choose e such that gcd(e, phi_n) == 1.
    phi_n = (p - 1) * (q - 1)

    # Since e is chosen randomly, we repeat the random choice
    # until e is coprime to phi_n.

    e = random.randint(2, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Choose d such that e * d % phi_n = 1.
    d = modular_inverse(e, phi_n)

    return ((p, q, d), (n, e))


def rsa_encrypt_text(public_key, plaintext):
    n, e = public_key

    encrypted = ''
    for letter in plaintext:
        # Note: we could have also used our rsa_encrypt function here instead
        encrypted = encrypted + chr((ord(letter) ** e) % n)

    return encrypted


def rsa_decrypt_text(private_key, ciphertext):
    p, q, d = private_key
    n = p * q

    decrypted = ''
    for letter in ciphertext:
        decrypted = decrypted + chr((ord(letter) ** d) % n)

    return decrypted


'''
priv,pub = rsa_generate_key(13,17)
print(priv)
print(pub)

cipher = rsa_encrypt_text(pub,"Abhishek")
print(cipher)

pt = rsa_decrypt_text(priv,cipher)
print(pt)
'''