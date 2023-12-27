def feistel_cipher(text, rounds, key):
    # Split the text into two halves
    left, right = text[:len(text)//2], text[len(text)//2:]

    # Feistel structure
    for round in range(rounds):
        # Apply a simple XOR operation with the key
        new_right = "".join(chr(ord(r) ^ ord(k)) for r, k in zip(right, key))

        # XOR the result with the left half
        new_right = "".join(chr(ord(r) ^ ord(l)) for r, l in zip(new_right, left))

        # Swap left and right for the next round
        left, right = right, new_right

    # Concatenate the final halves
    encrypted_text = left + right
    return encrypted_text

def feistel_decipher(ciphertext, rounds, key):
    # Split the ciphertext into two halves
    left, right = ciphertext[:len(ciphertext)//2], ciphertext[len(ciphertext)//2:]

    # Feistel structure in reverse
    for round in range(rounds):
        # XOR the right half with the key
        new_left = "".join(chr(ord(l) ^ ord(k)) for l, k in zip(left, key))

        # XOR the result with the original left half
        new_left = "".join(chr(ord(l) ^ ord(r)) for l, r in zip(new_left, right))

        # Swap left and right for the next round
        left, right = new_left, left

    # Concatenate the final halves
    decrypted_text = left + right
    return decrypted_text

# Example usage
plaintext = "Keep this Message "
key = "secretkey"
rounds = 16

# Encrypt the plaintext
encrypted_text = feistel_cipher(plaintext, rounds, key)
print("Encrypted Text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = feistel_decipher(encrypted_text, rounds, key)
print("Decrypted Text:", decrypted_text)
