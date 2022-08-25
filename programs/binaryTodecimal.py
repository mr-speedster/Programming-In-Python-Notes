binary = "10101"
exponent = len(binary)
decimal = 0
for x in binary:
    decimal += int(x)*2**(exponent-1)
    exponent -= 1
print(decimal)
