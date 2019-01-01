champC = ""
for i in range(1, 1000000):
	champC += str(i)
champC = [int(i) for i in champC]
total = champC[0]
for i in range(1,7): 
	# subtract 1 for 0 based indexing
	# print champC[(10**i)-1]
	total *= champC[(10**i)-1]

print total
