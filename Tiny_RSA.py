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


key = RSA_Keygenerator()

print key.public_key
print key.private_key
