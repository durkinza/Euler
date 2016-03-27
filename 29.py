Mnum = 100
mnum = 2
arr = []
arr2 = []
for i in range(mnum, Mnum+1):
    for j in range(mnum, Mnum+1):
        arr.append(str(i**j))
for a in arr:
    if not(a in arr2):
        arr2.append(a)
print len(arr2)
