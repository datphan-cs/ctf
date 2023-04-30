from pwn import *
from random import randint
from Crypto.Cipher import Salsa20
import string
import time
charac_list = string.ascii_letters + "0123456789_}{@!?-"
# print(charac_list)
flag = ''
known_char =[]

conn = remote('mercury.picoctf.net', 4572)
flag_line = conn.recvline().decode().rstrip()
enc_flag = flag_line[6:]
conn.recvline()
conn.recvline()

while '}' not in flag:
    for i in charac_list:
        to_send = flag + i
        conn.sendafter('me: ', to_send+'\n')
        line = conn.recvline(keepends=False).decode().rstrip().split('Here you go: ')[1]
        for text in known_char:
            line = line.replace(text,'')
        if line in enc_flag:
            enc_flag = enc_flag.replace(line,'')
            known_char.append(line)
            flag+=i
            print(flag)
            break
    time.sleep(2)
    if i == '-':
        print('error')