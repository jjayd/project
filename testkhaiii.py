from khaiii import KhaiiiApi
api = KhaiiiApi()
f = open('./input3.txt','r')
time = f.readline()
press = f.readline()
print(time,press)
total = []
cnt=0
while True:
    line = f.readline()
    if not line: break
    for word in api.analyze(line):
        words = str(word).split()
        for tmp in words:
            if 'NNG' in tmp:
                cnt=cnt+1
                ttmp = tmp.split('/')
                total.append(ttmp[0])
print(total)

