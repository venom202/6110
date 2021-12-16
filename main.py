'''
RSA cypher
'''

import Message_Encrypt as me
import Message_Decrypt as md
import signature_encrypt as se
import signature_decrypt as sd

class RSA:
    prime_numbers = []
    hex_list = []
    int_list = []

    '''# Generate P an Q values
    def generate_P_Q(self):
        # num = random.randrange(1,65535)
        for i in range(1, 65535):
            if (self.isPrime(i) == True) and (i.bit_length() == 16):
                self.prime_numbers.append(i)
        # print(prime_numbers)                    #Print list of 16 bits prime numbers
        p = random.choice(self.prime_numbers)
        q = random.choice(self.prime_numbers)
        if p == q:
            q = random.choice(self.prime_numbers)
            #print(f"P = {p}")
            #print(f"Q = {q}")
            return p,q
        else:
            #print(f"P = {p}")
            #print(f"Q = {q}")
            return p,q

    # Calculate N and Phi_N
    def n_and_phi_N(self, p, q):
        N = p * q
        print(f"N = {N}")
        phi_N = (p-1)*(q-1)
        print(f"Phi_N = {phi_N}")
        return N, phi_N

    # Prime number checker
    def isPrime(self, number):
        if number <= 1 or (number % 2 == 0 and number > 2):
            return False
        return all(number % i for i in range(3, int(m.sqrt(number)) + 1, 2))

    def generate_e(self, phi_N):
        while True:
            e = random.choice(RSA.prime_numbers)
            if e < phi_N:
                print(f"e = {e} \n================================================")
                return e
            else:
                continue
                
    def modInverse(a = 37693, m = 1615912200):
        for x in range(1, m):
            if (((a % m) * (x % m)) % m == 1):
                return x
        return -1
    print(modInverse())'''


#find GCD
    def GCD(self, e, phi_N):
        if e > phi_N:  # define the if condition
            temp = phi_N
        else:
            temp = e
        for i in range(1, temp + 1):
            if ((e % i == 0) and (phi_N % i == 0)):
                gcd = i
        #print(f"GCD ( {e}, {phi_N} ) = {gcd}")
        return gcd


#Convert to hexadecimal and integer values
    def convert_message_HEX_and_INT(self):
        m = "RSA concordia"                           # For signature change input to = Mehul
        m_chunk_list = list([m[i:i + 3] for i in range(0, len(m), 3)])
        print(f"MY_MESSAGE = {m}")
        print(f"MY_MESSAGE_chunks = {m_chunk_list}")
        for i in m_chunk_list:                                 # Convert to HEX
            s = i.encode('utf-8')
            hex_str = s.hex()
            self.hex_list.append("0x"+hex_str)
        #print(f"HEXADECIMAL VALUES = {self.hex_list}")
        for j in self.hex_list:
            self.int_list.append(int(j, 16))
        #print("INTEGER VALUES = {}".format(self.int_list))





print("#IDs")
print("MY_ID = 40191499")
print("PARTNER_ID = 40199530")
print("\n#my data")
print("p = 44101")
print("q = 36643")
print("N = 1615992943")
print("Phi_N = 1615912200")
print("e = 37693")
print("d = 219710557")
print("\n#my partner data")
print("PARTNER_N = 3502857563")
print("PARTNER_e = 87623")
print("\n#encryption")
r = RSA()
r.convert_message_HEX_and_INT()
me.encryption()
print("\n#decryption")
md.decryption()
print("\n#sign")
se.convert_message_HEX_and_INT()
se.signature_encryption()
print("\n#verify the signature")
sd.signature_decryption()

try:
    gcd = r.GCD(37693, 1615912200)
except ZeroDivisionError:
    CRED = '\033[91m'
    CEND = '\033[0m'
    print(CRED + "GCD is 0. Please try with different values of (e) and (Phi_N)" + CEND)


