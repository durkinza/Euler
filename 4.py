num2 = 100
while num2 < 1000:
    num2 = num2 + 1
    num1 = 100
    while num1 < 1000:
        num1 = num1 + 1
        st = str(num1 * num2)
        if(st == st[::-1]):
            print st

