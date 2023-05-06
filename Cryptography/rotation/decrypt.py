import string

UPPERCASE, LOWERCASE = string.ascii_uppercase, string.ascii_lowercase
OFFSET_UP, OFFSET_LOW = ord("A"), ord("a")

with open("encrypted.txt", "r") as file:
    ciphertext = file.readline().strip()


for i in range(1,26):
    possible_flag = ""
    for char in ciphertext:
        if char.islower():
            possible_flag += LOWERCASE[(ord(char) - OFFSET_LOW + i)%26]
        elif char.isupper():
            possible_flag += UPPERCASE[(ord(char) - OFFSET_UP + i)%26]
        else:
            possible_flag += char
    if "picoCTF" in possible_flag:
        print(possible_flag)
        break
