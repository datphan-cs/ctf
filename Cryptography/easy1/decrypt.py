import string

UPPERCASE = string.ascii_uppercase
OFFSET = ord("A")

ciphertext = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

flag = ""
for i in range(0,len(ciphertext)):
    idx_ciphertext = ord(ciphertext[i]) - OFFSET
    idx_key = ord(key[i]) - OFFSET
    flag += UPPERCASE[(idx_ciphertext - idx_key)%26]
print(f"picoCTF{{{flag}}}")