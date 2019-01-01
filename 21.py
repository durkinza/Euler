from functools import reduce
def factors(n):
    step = 2 if n%2 else 1
    li = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1, step) if n % i == 0)))
    if li is not None:
        li.remove(n)
    return list(li)

def find_am(a):
	fctrs = factors(a)
	b = 0
	for i in fctrs:
		b += i
	return b	

def is_amicable (a, b):
	# a != b so we can remove those amicable numbers
	if (a == b):
		return False
	# for our case, find_am(a) == b is already tested by the creation of b in the main function
	if find_am(b) == a:
		return True
	return False

# find all amicable numbers under 10000 where a != b
amicable = []
for a in range (2, 10000):
	b = find_am(a)
	if is_amicable(a, b):
		amicable.append(a)
		amicable.append(b)

# remove duplicate amicable number sets
unique = list(set(amicable))
# find the sum of the amicable numbers
total = 0
for i in unique:
	total += i
print(total)
