import string
dictionary = '.' + string.ascii_uppercase + string.digits + '_'
with open("message.txt", "r") as file:
    num_list = file.readline().split(" ")[:-1]
    
num_list = list(map(lambda x: pow(int(x),-1,41), num_list))

flag = ''.join(dictionary[num] for num in num_list)

print(f"picoCTF{{{flag}}}")