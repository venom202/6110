signature_int = [5072232, 30060]
final_signature_value = []
hex_list = []
int_list = []
m_chunk_list = []
m = "Mehul"

def convert_message_HEX_and_INT():
    m = "Mehul"
    print(f"MY_MESSAGE_TO_BE_SIGNED= {m}")
    m_chunk_list = list([m[i:i + 3] for i in range(0, len(m), 3)])
    for i in m_chunk_list:  # Convert to HEX
        s = i.encode('utf-8')
        hex_str = s.hex()
        hex_list.append("0x" + hex_str)
    #print(f"HEXADECIMAL VALUES = {hex_list}")
    for j in hex_list:
        int_list.append(int(j, 16))
    #print("INTEGER VALUES = {}".format(int_list))
    print(f"MY_MESSAGE_TO_BE_SIGNED_chunks = {m_chunk_list}")



def sig(s , d = 219710557, n = 1615992943):
    r = 1
    bits = list(bin(d)[2:])
    for bit in bits:
        r = (r * r) % n
        if int(bit) == 1:
            r = (r * s) % n
    return r

def signature_encryption():
    for i in range(len(signature_int)):
        sig_value = sig(signature_int[i])
        final_signature_value.append(sig_value)
    print(f"MY_SIGNATURE = {final_signature_value}")


#convert_message_HEX_and_INT()
#signature_encryption()
