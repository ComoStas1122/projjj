#!/usr/bin/env sage -python
from sage.all import *


def create_random_response(n): return random_vector(GF(2), n) # creating PUF response

def init_mechanism():
    '''
    Initiating The mechanism
    :ret: returning tuple containing (PUF, helper_data, H, res)
    '''

    helper_data = []
    n = int(input("Enter reponse len : "))
    F = GF(2)**n
    PUF = channels.QarySymmetricChannel(F, 0.1) # Creating the PUF
    res = PUF(create_random_response(n)) # PUF response
    print(f"PUF reponse : {res}")
    t = int(input("Enter desired error corrections : "))
    k = n-(t * 2 + 1)
    while True:
        code = codes.random_linear_code(GF(2), n, k)
        decoder = codes.decoders.LinearCodeSyndromeDecoder(code, t)
        if 'always-succeed' in decoder.decoder_type():
            break
        input()
        print(decoder, decoder.decoder_type())
    H = code.dual_code()
    print(f"Generated H => \n{H.generator_matrix()}")
    helper_data.append(H.generator_matrix() * res)
    return {"PUF" : PUF, "helper_data" : helper_data, "H" : (H, decoder.syndrome_table()), "response" : res}


def print_system(**system):
    '''
    Printing The system
    '''

    print(f"PUF => {system['PUF']}")
    print(f"Helper-Data => {system['helper_data']}")
    print(f"H => \n{system['H'][0].generator_matrix()}")
    
   
def gen_res(**system): return system['PUF'](system['response'])


def response_processing(res, **system):
    '''
    Function that processes the response
    :ret: True/False
    '''
    
    syndrome = system['H'][0].generator_matrix() * res
    print(res)
    print(f"Syndrome = > {syndrome}")
    for syn in system['H'][1]:
        xored_syn = syn + syndrome
        for data in system['helper_data']:
            if data == xored_syn:
                return True
    return False
    


if __name__ == "__main__":
    system = init_mechanism()
    print_system(**system)
    res = gen_res(**system)
    print(response_processing(res, **system))
