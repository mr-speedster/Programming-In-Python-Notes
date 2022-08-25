ch  = "dmlwk"
distance = 3
code = ""
for x in ch:
    value = ord(x) - distance
    if value < ord('a'):
        value = value + 26
    code = code + chr(value)
print(code)

#output : ajith