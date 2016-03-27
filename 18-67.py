tri = []
with open('p067_triangle.txt') as inputfile:
    for line in inputfile:
        tri.append(line.strip().split(' '))
for i in range(len(tri)-1, 0, -1):
    for j in range(0, len(tri[i])-1):
        num1 = (int(tri[i][j]) + int(tri[i-1][j]))
        num2 = (int(tri[i][j+1]) + int(tri[i-1][j]))
        if (num1 > num2):
            tri[i-1][j] = num1
        else:
            tri[i-1][j] = num2
        #print('['+str(i-1)+']['+str(j)+']'+' 1:'+str(num1)+' 2:'+str(num2)+'  ->'+str(tri[i-1][j]))
print tri[0][0]
