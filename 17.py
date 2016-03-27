ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

k = 0
# for i in ones:
#    k = k + len(i)
for i in teens:
    k = k + len(i)
    print (i+'  -> '+str(len(i)))
for i in tens:
    for j in ones:
        k = k+len(i+j)
        print (i+j+'  -> '+str(len(i+j)))
for h in range(1, len(ones)):
    k = k + len(ones[h]+'hundred')
    print(ones[h]+'hundred'+'  -> '+str(len(ones[h]+'hundred')))
    for i in teens:
        k = k + len(ones[h]+'hundredand'+i)
        print(ones[h]+'hundredand'+i+ '  -> '+str(len(ones[h]+'hundredand'+i)))
    # for i in range(1,len(tens)):
    #    k = k + len(ones[h]+'hundredand'+tens[i])
    #    print (ones[h]+' hundred and '+tens[i])
    for i in tens:
        if(i != ''):
            k = k + len(ones[h]+'hundredand'+i)
            print(ones[h]+'hundredand'+i+'  -> '+str(len(ones[h]+'hundredand'+i)))
        for j in range(1,len(ones)):
            print (ones[h]+'hundredand'+i+ones[j]+'  -> '+str(len(ones[h]+'hundredand'+i+ones[j])))
            k = k +len(ones[h]+'hundredand'+i+ones[j])
k = k + len('onethousand')
print('onethousand')
print k

