import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def check_password(user_input):
  if user_input == "happychance":
    return True
  else:
    print("That password is incorrect")
    sys.exit(0)
    return False
def get_flag(arg444):
  return decrypt(arg444.decode(), "rapscallion")
def prompt():
  return input("Please enter correct password for flag:")
def read_flag():
  return open('flag.txt.enc', 'rb').read()
def win():
  print("Welcome back... your flag, user:")
def decrypt(enc_flag, key):
    key_copy = key
    i = 0
    while len(key_copy) < len(enc_flag):
        key_copy = key_copy + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(flag_char) ^ ord(key_char)) for (flag_char,key_char) in zip(enc_flag,key_copy)])
flag_file = read_flag()
user_input = prompt()
check_password(user_input)
win()
flag = get_flag(flag_file)
print(flag)
sys.exit(0)

