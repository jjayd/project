r = open('2016-10-20.index_new','r')
q = open('newsinput.txt','r')
k = '"'
m = '","'

a = r.readline()
a=a.split()
x = q.readline()
old = a[2]

while True:
    text=""
    title = x[:-1]
    contents = x[:-1]
    sec = old
    while True:
        a = r.readline()
        a = a.split()
        x = q.readline()
        if "FINISH" in a:
            break
        new=a[2]
        if old==new:
            contents += x[:-1]
        else:
            old = new
            break
  #  a = r.readline()
  #  x = q.readline()
  #  x=x[:-1]
    if "FINISH" in a:
        break
  #  a=a.split()
    text = k+title+ m +contents+ m +a[0]+ m +str(sec)+k
    print(text)
