import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from gensim.models.wrappers import FastText
from gensim.models import KeyedVectors

#ko_model - Keyed

#model = FastText.load_fasttext_format('wiki.ko.bin')


#X= -2 * np.random.rand(100,2)
#X1 = 1 + 2 * np.random.rand(50,2)
#X[50:100, :] = X1
#k=2
#kmeans = KMeans(n_clusters=k).fit(X)
#print(kmeans.labels_)
empty=[0]*300

# Creating the model
ko_model = KeyedVectors.load_word2vec_format('wiki.ko.vec')
#model = FastText.load_fasttext_format('wiki.ko.bin')
#ko_model.save('fasttext.model')

# Getting the tokens
print("finish")
words = []
cnt=0
data=[]
f=open('keywordslist.txt','r')
while True:
    line = f.readline()
    if not line: break
    words=line.split()
    tmp=[]
    for i in range(10):
        print(words[i])
       # print(model.wv.get_vector(words[i]))
        if not words[i]:
            if i!=0:
                tmp.append(ko_model.wv.get_vector(words[i-1]))
            else:
                tmp.append(empty)
        else:
            tmp.append(ko_model.wv.get_vector(words[i]))
    data.append(tmp)
     #   print(ko_model[words])
print(data)
'''        
for word in ko_model.vocab:
    if cnt==10: break
    words.append(word)
    print(word)
    # Printing out number of tokens available
    print("Number of Tokens: {}".format(len(words)))

    # Printing out the dimension of a word vector
    print("Dimension of a word vector: {}".format(len(ko_model[words[0]])))

    # Print out the vector of a word
    print("Vector components of a word: {}".format(ko_model[words[0]]))
    print(words[0])
    cnt=cnt+1
    
k=3
data = [[1,1,1,1],[0,1,1,1],[2,2,3,2],[1,0,0,1]]
kmeans = KMeans(n_clusters=k).fit(data)
print(kmeans.labels_)
'''
