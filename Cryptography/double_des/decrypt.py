#!/usr/bin/python3 -u
from Crypto.Cipher import DES
from binascii import hexlify, unhexlify


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def double_encrypt(m):
    msg = pad(m)

    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()

ciphertext = "b2cab184e3c938aea852f46409b8780d38c1b25a010f313e0d21a22271cc777b712524fbe10f9ccb"
dict1 = {}
list2 = []

known_plaintext= "picoCTF{"
chosen_ciphertext = bytes.fromhex(ciphertext[:16])

for i in range(0, 1000000):
    key = pad("{0:06d}".format(i))
    print(f"Current key is {key}")    
    input2 = chosen_ciphertext
    cipher2 = DES.new(key, DES.MODE_ECB)
    list2.append(hexlify(cipher2.decrypt(input2)).decode())
    
for j in range(0, 1000000):
    key = pad("{0:06d}".format(j))
    print(f"Current key is {key}")    
    input1 = pad(known_plaintext)
    cipher1 = DES.new(key, DES.MODE_ECB)
    output = hexlify(cipher1.encrypt(input1)).decode()
    if output in list2:
        print(f"KEY1 is {key}")
        print(f"KEY2 is {list2.index(output)}")
        break

# cipher2 = DES.new(KEY2, DES.MODE_ECB)
# inter_text = cipher2.decrypt(bytes.fromhex(ciphertext))
# cipher1 = DES.new(KEY1, DES.MODE_ECB)
# flag = cipher1.decrypt(inter_text)

# print(hexlify(flag).decode())