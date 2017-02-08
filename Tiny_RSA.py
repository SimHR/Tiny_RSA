from ctypes import cdll
import time


class RSA_Keygenerator:
    key_func_lib = cdll.LoadLibrary("/home/shr/Desktop/Project/RSA/key_func.so")

    prime_generator = key_func_lib.prime_generator
    find_copirme = key_func_lib.find_coprime
    find_mod_inverse = key_func_lib.find_mod_inverse

    prime_num1 = prime_generator()
    time.sleep(1)
    prime_num2 = prime_generator()

    oiler_p = (prime_num1 - 1) * (prime_num2 - 1)
    N = prime_num1 * prime_num2
    e = find_copirme(oiler_p)
    d = find_mod_inverse(e, oiler_p)

    public_key = [N, e]
    private_key = [N, d]


def encrypte(raw_string, public_key):
    enc_string = [0, ]
    k = 0

    for i in raw_string:
        j = ord(i)

        if k == 0:
            enc_string[k] = (j ** public_key[1]) % public_key[0]
            k += 1

        else:
            enc_string.append((j ** public_key[1]) % public_key[0])
            k += 1

    return enc_string


def decrypte(enc_string, private_key):
    dec_string = [0, ]
    k = 0

    for i in enc_string:
        if k == 0:
            dec_string[0] = ((i ** private_key[1]) % private_key[0])
            k += 1

        else:
            dec_string.append((i ** private_key[1]) % private_key[0])
            k += 1

    return dec_string


key = RSA_Keygenerator()

string = raw_input("Please input any string:")

encrypted_string = encrypte(string, key.public_key)
print encrypted_string

decrypted_string = decrypte(encrypted_string, key.private_key)
print decrypted_string
