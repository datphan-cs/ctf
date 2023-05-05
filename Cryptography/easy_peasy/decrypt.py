from pwn import *
from binascii import unhexlify

KEY_LENGTH = 50000
MAX_SIZE = 1024

conn = remote("mercury.picoctf.net", port=20266)

conn.recvuntil(b"This is the encrypted flag!\n")
hex_flag = conn.recvline(keepends = False)
string_flag = unhexlify(hex_flag).decode()

left_to_send = KEY_LENGTH - len(string_flag)
while left_to_send > 0:
    print(f"Current left bytes is {left_to_send}")
    num_bytes_to_send = min(MAX_SIZE, left_to_send)
    conn.sendlineafter(b"What data would you like to encrypt?", b"a"*num_bytes_to_send)
    left_to_send -= MAX_SIZE
    
conn.sendlineafter(b"What data would you like to encrypt?", string_flag.encode())
conn.recvline()
flag = conn.recvline(keepends = False)

print(unhexlify(flag).decode())

conn.close()