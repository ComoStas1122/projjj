#!/usr/bin/env python3
from random import choice

POOL = ['0', '1']


def get_opposite(bit):
    if bit == '0':
        return '1'
    return '0'


def bits_seq(n=None, seq=None):
    '''
    :this function generates a bits sequence with a chance \\
            of being different in 0.01 chance in each bit
    :if no seq was provided, then a first random seq is generated
    :param - n: length of the sequence
    :ret - seq: sequence of n bits
    '''

    if not n and not seq:
        return []

    if not seq:
        seq = [choice(POOL) for _ in range(n)]
        return "".join(seq)

    seq = [get_opposite(bit) if choice(range(1, 100)) == 1 else bit
           for bit in seq]
    return "".join(seq)


if __name__ == "__main__":
    print("initial reposone -> ", init_seq := bits_seq(10))
    print(bits_seq(seq=init_seq))
