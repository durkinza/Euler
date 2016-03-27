z = 20
arr = [[0 for i in xrange(z+1)] for i in xrange(z+1)]
# set boarders
for i in range(0, z):
    arr[i][z] = 1
    arr[z][i] = 1
for i in range((z-1), -1, -1):
    for j in range((z-1), -1, -1):
        arr[i][j] = arr[i+1][j]+arr[i][j+1]
print arr
print arr[0][0]
