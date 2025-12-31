from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Kunci DES (8 byte = 64 bit, tapi efektif 56 bit)
key = b'12345678'
data = b'KRIPTOGRAFI'

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(data, 8))

print("Plaintext :", data)
print("Key       :", key)
print("Ciphertext:", binascii.hexlify(ciphertext))