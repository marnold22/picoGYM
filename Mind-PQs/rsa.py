#!/usr/bin/env python3

# NOTES:
# The public key is represented by the integers n and e
# The private key is represented by the integer d

# STEPS:
# 1. Need two distinct prime numbers (p & q)
# 2. Compute n = pq
# 3. Calculate the totient function -> phi(n)=(p−1)(q−1)
# 4. Select an integer e, such that e is co-prime to phi(n), and 1 < e < phi(n)
# 5. ed = 1 mod phi(n)

# (n, e) is the public key
# (n, d) is the private key

# c = message encoded 
encryptedText = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
# n = p*q
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
# e is > 1 and a co-prime of phi
e = 65537

# factoring n into p & q ->https://www.alpertron.com.ar/ECM.HTM
p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

# Phi is the totient
phi = (p-1)*(q-1)


# Encrypt -> C = P^e mod n
# Decrypt -> P = C^d mod n
# Need to calculate d

# Found on stack overflow - credit: Märt Bakhoff
# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m


# Found out that the pow function in python 3.8+ does the same as function above - credit: Märt Bakhoff
d = pow(e, -1, phi)

# Decrypt -> P = C^d mod n
decryptedText = pow(encryptedText, d, n)
print(decryptedText)
hexFlag = hex(decryptedText)
flag = bytearray.fromhex(hexFlag[2:]).decode()
print(flag)