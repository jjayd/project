crit  = open('./outtfdf.txt','r')
nowords=[]
while True:
    a = crit.readline()
    if not a: break
    nowords.append(a[:-1])
print(nowords)
for num in range(1,11):
    tmpin = 'text/out'+str(num)+'.txt'
    tmpout = 'text/reout'+str(num)+'.txt'
    
    f = open(tmpin,'r')
    f2 = open(tmpout,'w')
    
    title = f.readline()
    f2.write(title)

    press = f.readline()
    f2.write(press)

    line = f.readline()
    words = line.split()
    for word in words:
        if word not in nowords:
            f2.write(word+" ")


