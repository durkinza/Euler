import itertools

a = '0123456789'
arr = []
for p in itertools.permutations(a, len(a)):
    # print "".join(p),
    arr.append("".join(p))
# print arr
print arr[999999]
