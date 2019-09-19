from khaiii import KhaiiiApi
import io
api = KhaiiiApi()

t = io.open('pre.txt',mode='r', encoding='utf-8')
#x = io.open('2016-10-20.index_new',mode='r', encoding='utf-8')
#nt = io.open('top5_txt',mode='w')

fin = ["EF","SF","EC","ㅋ"]
label = ["NNG","W","MAG","VA","NNP"]
cnt=0
while True:
    text = t.readline()
    total=""
    if text=="\n":
        print()
        continue
    if "FINISH" in text:
        break
    print(cnt)
    for word in api.analyze(text):
        tmp = str(word)
        print(tmp)
        if any(format in tmp for format in label):
            chk=0
            if any(format in tmp for format in fin):
                chk=1
            ttmp = tmp.split()
            if chk==1:
                ttmp[0]=ttmp[0]+"."
            total=total+" "+ttmp[0]
    print()
    print()
    cnt+=1
#    print(total)
