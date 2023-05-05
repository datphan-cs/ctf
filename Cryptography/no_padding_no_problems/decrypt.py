from binascii import unhexlify
from pwn import *

conn = remote("mercury.picoctf.net", 30048)
conn.recvuntil(b"Good Luck!\n\n\n")

n = int(conn.recvline(keepends = False).decode().split(': ')[1])
e = int(conn.recvline(keepends = False).decode().split(': ')[1])
c = int(conn.recvline(keepends = False).decode().split(': ')[1])

fake_ciphertext = c + n
conn.sendlineafter(b"Give me ciphertext ", str(fake_ciphertext))

m = int(conn.recvline(keepends = False).decode().split(': ')[2])
flag = unhexlify(hex(m)[2:]).decode()
print(flag)
conn.close()