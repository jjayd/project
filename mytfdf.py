import io
import re

def f(t, d):
    # d: document
    return d.count(t)

def tf(t,d):
    return 0.5 + 0.5*f(t,d)/max([f(w,d) for w in d])

def df(t,D):
    numerator = len(D)
    denominator = 1+ len([True for d in D if t in d])
    return (denominator/numerator)

def tfdf(t,d,D):
    return tf(t,d)*df(t,D)

def tokenizer(d):
    return d.split()

def tfdfScorer(D):
    tokenized_D = [tokenizer(d) for d in D]
    result=[]
    for d in tokenized_D:
        result.append([(t,tfdf(t,d,tokenized_D)) for t in d])
    return result

if __name__ == '__main__':
    r=[]
    day = []
    company = []
    listwords = []
    X = []
    for i in range(1,11,1):
        tmp = 'text/out'+str(i)+'.txt'
        r.append(io.open(tmp,mode='r',encoding='utf-8'))

    for i in range(1,11,1):
        day.append(r[i-1].readline())
        company.append(r[i-1].readline())
        line = r[i-1].readline()
        listwords.append(line)

    corpus = listwords
    
    for i, doc in enumerate(tfdfScorer(corpus)):
    #    print('===== document[%d] ====='%i)
        doc = list(set(doc))
        doc.sort(key = lambda element : element[1])
        for a in doc:
            if a[1]>0.4:
                X.append(a[0])
        
    X = list(set(X))
    for i in X:
        print(i)
