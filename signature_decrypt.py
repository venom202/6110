signature_int = [711054654, 2454232689]
hex_list = []
final_signature_list = []
partner_message = "Surya"

def sig(s , d = 87623, n = 3502857563):
    r = 1
    bits = list(bin(d)[2:])
    for bit in bits:
        r = (r * r) % n
        if int(bit) == 1:
            r = (r * s) % n
    return r

def signature_decryption():
    print(f"PARTNER_SIGNED_MESSAGE = {partner_message}")
    print(f"PARTNER_SIGNATURE = {signature_int}")
    str = ""
    for i in range(len(signature_int)):
        sig_value = sig(signature_int[i])
        hex_value = hex(sig_value).replace("0x", "")
        #print(hex_value)
        hex_list.append(hex_value)
        byte_objects = bytes.fromhex(hex_value)
        final_string = byte_objects.decode("ASCII")
        #print(final_string)
        final_signature_list.append(final_string)
    #print(f"HEXADECIMAL VALUE = {hex_list}")
    #print(f"DECODED VALUE = {final_signature_list}")


    for obj in final_signature_list:
        str += obj
    #print(f"Decrypted Signature Sting = {str}")

    if str == partner_message:
        print("IS_VALID_SIGNATURE = True")
    else:
        print("IS_VALID_SIGNATURE = False")



#signature_decryption()
