total=0
for i in range(1, 1001):
	# print i
	total += i**i
s=[i for i in str(total)]
print s[-10:]
