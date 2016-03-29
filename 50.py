def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def isPrime(Number):
    return 2 in [Number, 2**Number % Number]

prmes = []


def find_lar():
    global prmes
    print ("Gerating primes")
    i = gen_primes()
    arr = []
    k = 0
    j = 0
    for x in i:
        prmes.append(x)
        k = k + x
        j = j + 1
        if (k > x) and isPrime(k):
            arr.append([k, j])
            # print(k, x, j)
        if k > 1000000:
            break
    return arr
"""

def find_next (snum, index):
    # starting from the current index, find the next largest prime number from the addition of
    # prime numbers
    a = [[snum,index]]
    for x in range(prmes[index], len(prmes)):
        snum += prmes[x]
        if isPrime(snum):
            if snum > prmes[x]:
                a.append([snum, x])
    return a

def up_one (minnum, sindex):
    # get minummum number of additions, and the current starting index
    arr = []

larget = 0
sindex = 0
number = 0
arr = []
i = gen_primes()
while (len(prmes)-sindex)>largest:
    k = 0


arr = find_lar()
largest = arr[-1]
i = gen_primes()
j = 1
for x in (largest[1]+1):
"""

find_lar()
i = gen_primes()
k = 0   # holds the current total number
j = 0   # holds the current total lenfth
largest = [0, 0]    # holds the largest chain number [number, length of chain]
sindex = 0          # holds the current index in the prmes array
while len(prmes) > sindex:
    k = 0
    j = 0
    for x in range(sindex, len(prmes)):
        k = k + prmes[x]
        j = j+1
        if isPrime(k):
            if k > prmes[x]:
                if j > largest[1]:
                    print str(k)+" - > "+str(j)
                    largest = [k, j]
        if k > 1000000:
            break
    sindex = sindex + 1
    print (largest)
    print sindex

print largest
