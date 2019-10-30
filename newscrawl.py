from newspaper import Article

f1 = open('urllist.txt','r')
while True:
    lines = f1.readline()
    if not lines:
        break
    word = lines.split()
    cate = word[0]
    cate2 = word[1]
    time  = word[2]
    url = word[3]
    a = Article(url,language='ko')
    a.download()
    a.parse()
    if not a.text:
        continue
    f = open('./text/news/input'+str(cate)+'-'+str(cate2)+'.txt','w')
    print(a.title)
    print(a.text)
    f.write(a.title)
    f.write(a.text)
