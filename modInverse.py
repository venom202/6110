def modInverse(a = 37693, m = 1615912200):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1
print(modInverse())
