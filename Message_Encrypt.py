int_list = [5395265, 2122607, 7234415, 7496809, 97]
final_decryption_list = []

def enc(a , e = 87623 , n = 3502857563):
    r = 1
    bits = list(bin(e)[2:])
    for bit in bits:
        r = (r * r) % n
        if int(bit) == 1:
            r = (r * a) % n
    return r


def encryption():
    for i in range(len(int_list)):
        dec_value = enc(int_list[i])
        final_decryption_list.append(dec_value)
    print(f"MY_CIPHERTEXT = {final_decryption_list}")

#encryption()




