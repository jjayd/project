import tfidf
import io
import re

if __name__ == "__main__":
    r1 = r= io.open('../out1.txt',mode='r', encoding='utf-8')
    r2 = r= io.open('../out2.txt',mode='r', encoding='utf-8')
    r3 = r= io.open('../out3.txt',mode='r', encoding='utf-8')

    day = r1.readline()
    company = r1.readline()
    line = r1.readline()
    listwords1 = line.replace("'",'').replace(' ','').replace('[','').replace(']','').split(',')
    print(listwords1)
    
    day = r2.readline()
    company = r2.readline()
    line = r2.readline()
    listwords2 = line.replace("'",'').replace(' ','').replace('[','').replace(']','').split(',')
    print(listwords2)

    day = r3.readline()
    company = r3.readline()
    line = r3.readline()
    listwords3 = line.replace("'",'').replace(' ','').replace('[','').replace(']','').split(',')
    print(listwords3)
    
    sim = table.similarities(["서울대","노조","재활용"])
    for s in sim:
        print(s)

