with open("message.txt","r") as file:
    ciphertext = file.readline().strip()
    
flag = ""

for i in range(0,len(ciphertext), 3):
    flag+= ciphertext[i+2] + ciphertext[i:i+2]
    
print(flag)