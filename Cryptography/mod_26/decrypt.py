import string
LOWERCASE =  string.ascii_lowercase
UPPERCASE =  string.ascii_uppercase

ciphertext = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"
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
                         
        