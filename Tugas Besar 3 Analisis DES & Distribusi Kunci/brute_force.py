from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

ciphertext = ciphertext

found = False

for i in range(100000):  # simulasi key space kecil
    trial_key = i.to_bytes(8, byteorder='big')
    cipher = DES.new(trial_key, DES.MODE_ECB)
    
    try:
        decrypted = unpad(cipher.decrypt(ciphertext), 8)
        if decrypted == b'KRIPTOGRAFI':
            print("KEY DITEMUKAN:", trial_key)
            found = True
            break
    except:
        pass

if not found:
    print("Key tidak ditemukan dalam ruang kunci terbatas (simulasi)")