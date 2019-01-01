from functools import reduce
def factors(n):
    step = 2 if n%2 else 1
    li = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1, step) if n % i == 0)))
    if li is not None:
        li.remove(n)
        return list(li)
	return list

def is_abundant(n):
    fctrs = factors(n)
    b = 0
    for i in fctrs:
        b += i
    if b > n:
        return True
    return False

def is_not_2_abundant(n):
	"""
	returns true if the number cannot be formed by the sum of 2 abundant numbers
	"""
	global abundants
	for i in abundants:
		j = n-i
		if j in abundants:
			return False
	return True

abundants = []
not_2_abundants = []
for i in range(2, 28123):
	if is_abundant(i):
		#print "is abundant: "+str(i)
		abundants.append(i)
	if is_not_2_abundant(i):
		#print "is not 2 abundants: "+str(i)
		not_2_abundants.append(i)

#print abundants
#print not_2_abundants

# start with 1 since 1 is not formed by 2 abundant numbers
total = 1
for i in not_2_abundants:
	total += i
print total
