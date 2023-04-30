from sympy import *
from binascii import unhexlify, hexlify
anger = 9649749624129728805411567825948207742414731330944001264264124635479741113877
envy = 12976591612217122697792686863585612942934694873968364943859725378374897036033
e = 65537
phi = e*envy-1
with open('test.txt','r') as file:
    list_div = file.readlines()

    list_div = list(map(lambda x: x.replace(',',''),list_div))
    list_div = [int(n) for n in list_div]
approve = []
for i in list_div:
    if isprime(i+1) and phi%i == 0:
        approve.append(i+1)
approve = list(filter(lambda x: x.bit_length()==128, approve))
        
for i in range (0, len(approve)):
    for j in range (i, len(approve)):
        n = approve[i]*approve[j]
        applicant = pow(anger,envy,n)
        try:
            value = unhexlify(hex(applicant)[2:])
            printable = all(chr(x).isprintable() for x in value)
            if printable:
                print(str(value))
        except:
            pass