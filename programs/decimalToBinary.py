decimal = 15
binary = ""
while decimal>0:
    rem = decimal % 2
    binary = binary + str(rem)
    decimal //= 2
print(binary)