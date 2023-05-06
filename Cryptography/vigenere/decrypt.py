import string

with open("cipher.txt", "r") as file:
    ciphertext = file.readline().strip()
    key = file.readline().strip()
    
UPPERCASE, LOWERCASE = list(string.ascii_uppercase), list(string.ascii_lowercase)
OFFSET_UP, OFFSET_LOW = ord("A"), ord("a")
KEY_LEN = len(key)

flag = ""
i,j = 0,0
while i < len(ciphertext):
    c = ciphertext[i]
    k = key[j % KEY_LEN]
    if c.islower():
        idx = (ord(c) - ord(k.lower()))%26
        flag += LOWERCASE[idx]
        j = (j + 1) % KEY_LEN
    elif c.isupper():
        idx = (ord(c) - ord(k))%26
        flag += UPPERCASE[idx]
        j = (j + 1) % KEY_LEN
    else:
        flag += c
    i = i + 1

print(flag)