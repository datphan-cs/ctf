import string


UPPERCASE = string.ascii_uppercase
encrypted_flag = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
flag = ""

def to_flag (flag):
    string_flag = ""
    for num in flag:
        string_flag += UPPERCASE[num]
    return string_flag


for i in range (1,26):
    rotated_flag = list(map(lambda x: (x + i)%26, encrypted_flag)) 
    possible = to_flag(rotated_flag)
    if "PICOCTF" in possible:
        print(possible[:7]+"{" + possible[7:] + "}")
        break
