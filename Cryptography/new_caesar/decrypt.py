import string

OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_decode(cipher):
    plain = ""
    for i in range (0, len(cipher),2):
        first = ord(cipher[i]) - OFFSET
        second = ord(cipher[i+1]) - OFFSET
        binary = "{0:04b}".format(first) + "{0:04b}".format(second) 
        plain += chr(int(binary, 2)) 
    return plain

def shift(c, k):
    t1 = ord(c) - OFFSET
    t2 = ord(k) - OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

ciphertext = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

for key in ALPHABET:
    possible_flag = ""
    for c in ciphertext:
        possible_flag += shift(c, key)
        
    possible_flag = b16_decode(possible_flag)
    
    if possible_flag.isprintable():
        print(possible_flag)

