num = 125
temp = num
reverse , sum = 0 , 0
while num > 0:
    rem = num%10
    num //= 10
    sum = sum + rem
    reverse = reverse * 10 + rem
print(sum , reverse)