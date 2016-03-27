l = 0
m = 0  # holds the answer
for i in range(1, 1000001):
    n = i
    k = 0
    print i
    while n > 1:
        k = k+1
        if(n%2 == 0):
            n = n/2
        else:
            n = ((3*n)+1)
        if k > l:
            l = k
            m = i
print str(m)+' -> '+str(l)
