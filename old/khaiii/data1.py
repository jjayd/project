from khaiii import KhaiiiApi
import io
api = KhaiiiApi()

t = io.open('pre.txt',mode='r', encoding='utf-8')
#x = io.open('2016-10-20.index_new',mode='r', encoding='utf-8')
#nt = io.open('top5_txt',mode='w')

fin = ["EF","SF","ㅋ","EC"]
label = ["NNG","VV","VA","NNP"]
cnt=0
while True:
    text = t.readline()
    total=""
    if text=="\n":
        print()
        continue
    if "FINISH" in text:
        break
    for word in api.analyze(text):
        tmp = str(word)
        if label[0] in tmp or label[1] in tmp or label[2] in tmp or label[3] in tmp and "하지만" not in tmp:
     #   if any(format in tmp for format in label):
            if cnt==226:
                print(tmp)
            chk=0
            if tmp[-2:] == "EF" or tmp[-2:] == "SF" or tmp[-2:]=="EC":
   #     if any(format in tmp for format in fin):
                chk=1
            ttmp = tmp.split()
            if chk==1:
                ttmp[0]=ttmp[0]+"\n"
            total=total+" "+ttmp[0]
    if cnt==226:
        print()
        print(total)
        print()
        break
    cnt+=1
#    print(total)
