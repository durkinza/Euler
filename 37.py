def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    # The running integer that's checked for primeness
    q = 2
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def is_truncable(n):
	global primes
	# count the digits in the number
	l = len(str(n))
	# creating a list of the digits
	li = [i for i in str(n)]
	# test for right to left and left to right truncability. 
	for i in range(1, l):
		# testing left to right truncability
		if int(str().join(li[:i])) not in primes:
			return False
		# testing right to left truncability
		if int(str().join(li[i:])) not in primes:
			return False
	print("found Truncable")
	print(n)
	return True


i = gen_primes()
primes = []
truncable = []

for j in i:
	primes.append(j)
	# primes 2, 3, 5, 7 won't count for truncability 
	if j < 9:
		continue
	if is_truncable(j):
		truncable.append(j)
	# only the first 11 truncable primes are needed
	if len(truncable) == 11:
		print(truncable)
		break
	# infinite loops aren't fun
	if j > 1000000000:
		print("nope")
		break

# sum the truncables for the final answer
total = 0
for i in truncable:
	total+=i
print total
