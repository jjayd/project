f2 = open('articles.txt','w')

for i in range(1,16,1):
    for j in range(1,4,1):
        t = "input"+str(i)+'-'+str(j)+'.txt'
        try:
            f=open(t,'r')
        except:
            continue
        lines=""
        while True:
            line = f.readline()
            if not line: break
            tmp = line.split('\n')
            for k in range(len(tmp)):
                tmp[k]=tmp[k].replace(",","")
                lines+=tmp[k]
        f2.write(lines)
        f2.write("\n")
