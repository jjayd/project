from khaiii import KhaiiiApi
import re

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text 

api = KhaiiiApi()

for num in range(1,11,1):
    tmpin = 'text/input'+str(num)+'.txt'
    tmpout = 'text/out'+str(num)+'.txt'
    print(num)

    f = open(tmpin,'r')
    f2 = open(tmpout,'w')
    time = f.readline()
    f2.write(time)
    press = f.readline()
    f2.write(press)
    total = []
    cnt=0
    while True:
        line = f.readline()
        line = cleanText(line) 
        if not line: break
        try:
            for word in api.analyze(str(line)): # api.analyze(line)
                words = str(word).split()

                for tmp in words:
                    if 'NNG' in tmp:
                        cnt=cnt+1
                        ttmp = tmp.split('/')
                        total.append(ttmp[0])
        except:
            pass

    print(total)
    for word in total:
        f2.write(word+" ")

