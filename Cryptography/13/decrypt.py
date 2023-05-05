import string
LOWERCASE =  string.ascii_lowercase
UPPERCASE =  string.ascii_uppercase

ciphertext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
flag = ""

for char in ciphertext:
    if char in LOWERCASE:
        idx = LOWERCASE.index(char)
        char = LOWERCASE[(idx+13)%26]
    elif char in UPPERCASE:
        idx = UPPERCASE.index(char)
        char = UPPERCASE[(idx+13)%26]
    flag += char
print(flag)
                         
        