# Simplified Diffie-Hellman Key Exchange
def diffie_hellman_key_exchange(p, g, a, b):
    A = (g ** a) % p  # Alice's public key
    B = (g ** b) % p  # Bob's public key

    shared_secret_Alice = (B ** a) % p  # Alice's shared secret
    shared_secret_Bob = (A ** b) % p  # Bob's shared secret

    return shared_secret_Alice, shared_secret_Bob


# Example parameters
p = 23  # Prime number
g = 5  # Primitive root modulo p

# Alice and Bob's private keys
private_key_Alice = 6
private_key_Bob = 15

# Exchange public keys
shared_secret_Alice, shared_secret_Bob = diffie_hellman_key_exchange(p, g, private_key_Alice, private_key_Bob)

print("Alice's Shared Secret:", shared_secret_Alice)
print("Bob's Shared Secret:", shared_secret_Bob)


# Eve intercepts the communication
def man_in_the_middle_attack(p, g, a, b, intercepted_public_Alice, intercepted_public_Bob):
    # Eve intercepts public keys and pretends to be Alice to Bob
    shared_secret_Alice = (intercepted_public_Bob ** a) % p

    # Eve intercepts public keys and pretends to be Bob to Alice
    shared_secret_Bob = (intercepted_public_Alice ** b) % p

    return shared_secret_Alice, shared_secret_Bob


# Eve intercepts public keys
intercepted_public_Alice = 9
intercepted_public_Bob = 7

# Eve performs the man-in-the-middle attack
shared_secret_Alice_mitm, shared_secret_Bob_mitm = man_in_the_middle_attack(p, g, private_key_Alice, private_key_Bob,
                                                                            intercepted_public_Alice,
                                                                            intercepted_public_Bob)

print("Eve's Interception - Alice's Shared Secret:", shared_secret_Alice_mitm)
print("Eve's Interception - Bob's Shared Secret:", shared_secret_Bob_mitm)
