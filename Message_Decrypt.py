enc_list = [1378680580,1564267064,46528309,287505561,168718151,334868354]
final_decryption_output = []

def dec(s , d = 219710557, phi_n = 1615992943):
    r = 1
    bits = list(bin(d)[2:])
    for bit in bits:
        r = (r * r) % phi_n
        if int(bit) == 1:
            r = (r * s) % phi_n
    #print(r)
    return r

def decryption():
    print(f"PARTNER_CIPHERTEXT = {enc_list}")
    output_list = []
    hex_list = []
    str = ""
    for i in range(len(enc_list)):
       # print(f"Encoded value = {enc_list[i]}")
        value = dec(enc_list[i])
        output_list.append(value)
        hex_value = hex(value).replace("0x","")
        #print(f"HEX Value = {hex_value}")
        hex_list.append(hex_value)
        byte_objects = bytes.fromhex(hex_value)
        final_string = byte_objects.decode("ASCII")
        #print(f"PARTNER_MESSAGE_chunks_AFTER_DECRYPT = {final_string}")
        final_decryption_output.append(final_string)
    print(f"PARTNER_MESSAGE_chunks_AFTER_DECRYPT = {final_decryption_output}")
    #print(hex_list)

    for obj in final_decryption_output:
        str += obj
    print(f"PARTNER_MESSAGE_AFTER_DECRYPT = {str}")


#decryption()