# import random

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def mod_inverse(a, m):
#     m0, x0, x1 = m, 0, 1
#     while a > 1:
#         q = a // m
#         m, a = a % m, m
#         x0, x1 = x1 - q * x0, x0
#     return x1 + m0 if x1 < 0 else x1

# p = 61 #11
# q = 53 #13
# n = p * q
# e = 17 
# phi = (p - 1) * (q - 1)

# while e < phi and gcd(e, phi) != 1:
#     e += 1

# d = mod_inverse(e, phi)

# msg = 50
# print("Message data = ", msg)

# # Encryption: c = (msg ^ e) % n
# ciphertext = pow(msg, e, n)
# print("Encrypted data = ", ciphertext)

# # Decryption: m = (c ^ d) % n
# plaintext = pow(ciphertext, d, n)
# print("Original Message Sent = ", plaintext)

import random
import math
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Generate random prime numbers p and q
p, q = 0, 0
while not is_prime(p):
    p = random.randint(50, 200)  # Adjust the range as needed
while not is_prime(q) or q == p:
    q = random.randint(50, 200)  # Adjust the range as needed

n = p * q
e = 17
phi = (p - 1) * (q - 1)

while e < phi and math.gcd(e, phi) != 1:
    e += 1

d = mod_inverse(e, phi)

msg = int(input("Enter the original message:"))
print("Message data = ", msg)

# Encryption: c = (msg ^ e) % n
ciphertext = pow(msg, e, n)
print("Encrypted data = ", ciphertext)

# Decryption: m = (c ^ d) % n
plaintext = pow(ciphertext, d, n)
print("Original Message Sent = ", plaintext)
