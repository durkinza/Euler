srt = []
k = 0
for i in range(1, 101):
    k = k + i
    s = i*i
    srt.append(s)
j = k*k
y = 0
for q in srt:
    y = y+q
print (j - y)
