import math
i=9
arr=[3,5,6,9]
while (i<999):
    i = i+1
    if (i%5==0) or (i%3==0):
        arr.append(i);
        print i
k = 0
for j in arr:
    k = k + j

print k

