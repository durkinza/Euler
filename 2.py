arr= [1,2]
i = 0
while i < 4000000:
    i = arr[-1]+arr[-2]
    arr.append(i)
    print i
k =0
for j in arr:
    if j %2 ==0:
        k = k+j
print k
