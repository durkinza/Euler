def get_denominators(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
j = 1
i = 1
while True:
    j = j + 1
    i = i + j
    k = len(get_denominators(i))
    if k > 500:
        print 'key is : '+str(i)+' -> '+str(k)
        break
    print str(i)+' -> '+str(k)
