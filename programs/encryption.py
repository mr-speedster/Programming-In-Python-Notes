ch = "ajith"
distance = 3
code = ""
for x in ch:
    value = ord(x) + distance
    if value > ord('z'):
        value = value-24
    code = code + chr(value)
print(code)


#output : dmlwk