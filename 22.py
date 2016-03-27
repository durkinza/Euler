names = []
f = open('p022_names.txt')
for i in f.read().split(','):
    names.append(i[1:-1])
names.sort()
# print names
k = 0
a = 0
b = 0
for i in range(0, len(names)):
    a = list(names[i])
    b = 0
    for j in a:
        if j.lower() == 'a': b +=1
        elif j.lower() == 'b': b+=2
        elif j.lower() == 'c': b+=3
        elif j.lower() == 'd': b+=4
        elif j.lower() == 'e': b+=5
        elif j.lower() == 'f': b+=6
        elif j.lower() == 'g': b+=7
        elif j.lower() == 'h': b+=8
        elif j.lower() == 'i': b+=9
        elif j.lower() == 'j': b+=10
        elif j.lower() == 'k': b+=11
        elif j.lower() == 'l': b+=12
        elif j.lower() == 'm': b+=13
        elif j.lower() == 'n': b+=14
        elif j.lower() == 'o': b+=15
        elif j.lower() == 'p': b+=16
        elif j.lower() == 'q': b+=17
        elif j.lower() == 'r': b+=18
        elif j.lower() == 's': b+=19
        elif j.lower() == 't': b+=20
        elif j.lower() == 'u': b+=21
        elif j.lower() == 'v': b+=22
        elif j.lower() == 'w': b+=23
        elif j.lower() == 'x': b+=24
        elif j.lower() == 'y': b+=25
        elif j.lower() == 'z': b+=26
    k = k+(b*(i+1))
print k
