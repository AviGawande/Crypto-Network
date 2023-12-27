from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# DES encryption
def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# DES decryption
def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Example usage
key = get_random_bytes(8)
plaintext = b"Hello123"
ciphertext = des_encrypt(plaintext, key)
decrypted_text = des_decrypt(ciphertext, key)

print("Original Text:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
