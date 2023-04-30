import math
import hashlib
import sys
from tqdm import tqdm
import functools
import numpy
from gmpy2 import *
from sympy import *

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfe7d7086e788af7922b")
MOD_VALUE = mpz(10**10000)

@functools.cache
def m_func(n):
    print(n)
    n = n - 3
    A = Matrix([
        [21, 301, -9549, 55692],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ])

    P,D = A.diagonalize()
    inv_P =P.inv()
    print(P)
    print(D)
    print(inv_P)
    start_matrix = Matrix([
        [4],
        [3],
        [2],
        [1]
    ])
    # print(D_n)
    first_half =Matrix([[1,0,0,0]])*P
    second_half =inv_P * start_matrix
    print(first_half)
    print(second_half)
    print(first_half * second_half)
    # res = numpy.matmul(test, start_matrix)
    # needed = res[0]
    # needed = mpz(needed)% MOD_VALUE
    return ( -4976244 * (mpz(-21)**n) + 565585920 * (mpz(12)**n)  - 792991771 * (mpz(13)**n) +232438943 * (mpz(17)**n) )//14212

# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = m_func(ITERS)
    # print(sol)
    decrypt_flag(sol)

