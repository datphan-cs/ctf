from pwnlib.tubes.remote import remote
import zlib
from binascii import unhexlify
from random import randint
import os
from Crypto.Cipher import Salsa20
import string
charac_list = string.ascii_lowercase + string.ascii_uppercase + '_}'
flag = 'picoCTF{sheriff_you_so'
max_len = 999
def compress(text):
    return zlib.compress(bytes(text.encode("utf-8")))

def encrypt(plaintext):
    secret = os.urandom(32)
    cipher = Salsa20.new(key=secret)
    return cipher.nonce + cipher.encrypt(plaintext)

conn = remote('mercury.picoctf.net', 50899)
while '}' not in flag:
    max_len = 999
    best =''
    for i in charac_list:
        try:
            conn.recvuntil(b"encrypted: ")
            conn.sendline((flag+i).encode())
            conn.recvline()
            conn.recvline() 
            line = int(conn.recvline().rstrip())
            if (line < max_len):
                max_len = line
                best = i
        except:
            conn = remote('mercury.picoctf.net', 50899)
    flag += best
    print(flag)
    