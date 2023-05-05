import string

LOWERCASE = string.ascii_lowercase
OFFSET = ord("a")
with open("ciphertext", "r") as file:
    ciphertext = file.read()

encrypted_part = ciphertext[ ciphertext.find('{') + 1 : -1]

for i in range(1,26):
    possible_flag = ""
    for char in encrypted_part:
        possible_flag += LOWERCASE[(ord(char) - OFFSET + i)%26]
    if "crossing" in possible_flag:
    	print(f"picoCTF{{{possible_flag}}}")
