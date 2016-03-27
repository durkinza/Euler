num = 100
i = num
k = 0
while k < num:
    j = num - k
    i = i * j
    k = k + 1

s = list(str(i))
k = 0
for i in s:
    k = k + int(i)
print k
