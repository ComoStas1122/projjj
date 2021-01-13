#!/usr/bin/env python3
import random_bit_seq_gen
import numpy as np


def handle_respone(resp):
    '''
    This Function handles the received PUF response \\
            using HARD Decision algorithm
    :resp: the PUF response
    :return flag:
    '''
    pass


def gen_mat(n, k):
    '''
    This Function generates a CHECK_MAT, given amount of errors, and resp_len
    :resp_len: length of the PUF response
    :err_num: maximum amount of errors in the PUF
    '''
    pass


def main():
    '''
    Main Handler Function
    :ret: True of ran well, 0 if not
    '''

    N = ""
    D = ""
    while not N.isdigit() and not D.isdigit():
        N = input("Enter the PUF reponse len: ")
        D = input("Enter maximum ERRORS possible: ")
        if N.isdigit() and D.isdigit() and int(N) <= int(D):
            continue
    N = int(N)
    D = int(D)
    resp = random_bit_seq_gen.bits_seq(n=N)
    print(f"Generated PUF Response is: {resp}")
    print(f"Generating a CHECK MATRIX GIVEN PARAMS : N = {N} NUM of errors "
          f"= {D}")


if __name__ == "__main__":
    main()
