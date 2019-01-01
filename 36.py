def is_palindrome(n):
	l = [i for i in str(n)]
	r = [i for i in reversed(str(n))]
	if l == r:
		return True
	return False

def is_palindromic(n):
	b = bin(n).lstrip("0b")
	return is_palindrome(b)



palindromics = []
for i in range(1, 1000000):
	if is_palindrome(i):
		if is_palindromic(i):
			palindromics.append(i)

#print(palindromics)

total = 0
for i in palindromics:
	total += i

print(total)
			
