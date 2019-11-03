from newspaper import Article
from datetime import datetime, timedelta
import hanja

f1 = open('urllist.txt','r')
timef = open('subtime.txt','w')
cnt=1
tcnt=1
timelist = []
while True:
    print(cnt,tcnt)
    cnt+=1
    tcnt+=1
    if tcnt==4:
        tcnt=1
    lines = f1.readline()
    if not lines:
        break
    word = lines.split()
    cate = word[0]
    cate2 = word[1]
    time  = "20"+word[2]
    realtime = datetime(int(time[0:4]),int(time[4:6]),int(time[6:]))
    pivot=datetime(2000,1,1)
    timef.write(str((realtime-pivot).days))
    timef.write('\n')
    
   # timelist.append(realtime)
    url = word[3]
    a = Article(url,language='ko')
    a.download()
    a.parse()
    if not a.text:
        continue
    f = open('./text/news/input'+str(cate)+'-'+str(cate2)+'.txt','w')
    #print(a.title)
    #print(a.text)
    title = hanja.translate(a.title,'substitution')
    f.write(title)
    f.write(".\n")
    text = hanja.translate(a.text,'substitution')
    f.write(text)
    

