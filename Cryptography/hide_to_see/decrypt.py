with open("encrypted.txt","r") as file:
    ciphertext = file.readline().strip()

n, N = ord('z') + ord('a'), ord('Z') + ord('A')
flag=''
for char in ciphertext:
	if char.islower():
		flag += chr(n-ord(char))
	elif char.isupper():
		flag += chr(N-ord(char))
	else:
		flag+= char
  
print(flag)
    
