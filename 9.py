num1 = 3
num2 = 4
num3 = 5
arr = []
while num3 < 500:
    num3 = num3 + 1
    num2 = 1
    num1 = 1
    print num3
    while num2 < 500:
        num2 = num2 + 1
        num1 = 1
        while num1 < 500:
            num1 = num1 + 1
            if(num1 + num2 + num3) == 1000:
                arr.append([num1, num2, num3])
print arr
for i in arr:
    if((i[0]*i[0])+(i[1]*i[1])) == (i[2]*i[2]):
        print i[0]*i[1]*i[2]
        break
