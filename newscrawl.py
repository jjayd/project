from newspaper import Article
url='https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=015&aid=0004212309&date=20190922&type=1&rankingSeq=9&rankingSectionId=101'
a = Article(url,language='ko')
a.download()
a.parse()
print(a.title)
print(a.text)
