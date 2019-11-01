fw= open('articles.txt','w')

for i in range(1,11):
    t = 'input'+str(i)+'.txt'
    f=open(t,'r')
    line = f.readline()
    line = f.readline()
    lines=""
    while True:
        line = f.readline()
        if not line: break
        tmp = line.split('\n')
        for j in range(len(tmp)):
            lines+=tmp[j]
    fw.write(lines)
    fw.write("\n")

