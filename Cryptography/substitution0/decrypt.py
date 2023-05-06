import string

ORI_ALPHABET = list(string.ascii_uppercase + string.ascii_lowercase)

with open("message.txt","r") as file:
    content = file.readlines()
    key = content[0].rstrip()
    ciphertext = content[-1].rstrip()

ROT_ALPHABET = list(key + key.lower())

dictionary = dict(zip(ROT_ALPHABET, ORI_ALPHABET))
flag = ""

for char in ciphertext:
    flag += dictionary[char] if char in dictionary else char

print(flag)

