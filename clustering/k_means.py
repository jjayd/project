# Tokenize and Stem Data
# Convert words to Vector Space using TFIDF matrix
# Using KMeans clustering to find out clusters
# Calculate Cosine Similarity and generate the distance matrix
# Dimensionality reduction using MDS to results the KMeans output
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import *
import os
from math import log10
from scipy.sparse import csr_matrix
from gensim.models import KeyedVectors

path = os.path.abspath(os.path.dirname(__file__))

allwords=[]

def f(t,d):
    return d.count(t)

def tf(t,d):
    return 0.5+0.5*f(t,d)/max([f(w,d) for w in d])

def idf(t,D):
    numerator = len(D)
    denominator = 1+len([True for d in D if t in d])
    return log10(numerator/denominator)

def tfidf(t,d,D):
    return tf(t,d)*idf(t,D)

def tokenizer(d):
    return d.split()

def tfidfScorer(D):
    tokenized_D = [tokenizer(d) for d in D]
    global allwords
    for d in tokenized_D:
        for t in d:
            allwords.append(t)
    allwords=list(set(allwords))
    allwords.sort()
    print(allwords)
    result = []
    for d in tokenized_D:
        tmp=[]
        for k in allwords:
            if k in d:
                tmp.append([k,tfidf(k,d,tokenized_D)])  
            else:
                tmp.append([k,0])
        result.append(tmp)
    #    result.append([(t,tfidf(t,d,tokenized_D)) for t in allwords])
    
    return result

#Instead of TfIdf Vectorizer

def applysim(m):
    model = KeyedVectors.load_word2vec_format('../wiki.ko.vec')
   # return m
    global allwords
    length = len(allwords)

    matrix = [[0]*length for i in range(length)]
    for i in range(length):
        for j in range(i+1,length):
            try:
                sim = model.wv.similarity(allwords[i],allwords[j])
            except:
                sim=0
            if sim>0.6:
                matrix[i][j]=sim
                matrix[j][i]=sim
            
#    print(matrix)
#    print()
    print("finish sim")
    for i in range(len(m)):
        for j in range(1,length):
            for k in range(j+1,length):
                if matrix[j][k]!=0:
            #        print(j,k)
           #         print(allwords[j],allwords[k],matrix[j][k])
          #          print(m[i][j],m[i][k])
                    if m[i][j]==0:
                        m[i][j]=m[i][k]*matrix[j][k]
                    elif m[i][k]==0:
                        m[i][k]=m[i][j]*matrix[j][k]
    return m

def weighted_tfidf(data):
    wtfidf=[]
    f = open('../subtime.txt','r')
    time=[]
    while True:
        line = f.readline()
        if not line: break
        time.append(int(line)/10000)
    for i,doc in enumerate(tfidfScorer(data)):
        tmp=[]
        tmp.append(time[i])
        for j in doc:
            tmp.append(j[1])
        wtfidf.append(tmp)
    wtfidf=applysim(wtfidf)
    wtfidf=np.asarray(wtfidf)
    return csr_matrix(wtfidf)

# Tokenizer to return stemmed words, we use this
def tokenize_and_stem(text_file):
    # declaring stemmer and stopwords language
    stemmer = SnowballStemmer("english")
    f = open('../outtfdf.txt')
    sw=[]
    while True:
        w=f.readline()
        if not w: break
        sw.append(w[:-1])
    stop_words=sw
 #   stop_words = set(stopwords.words('english'))
    words = word_tokenize(text_file)
    filtered = [w for w in words if w not in stop_words]
    stems = [stemmer.stem(t) for t in filtered]
#    print(stems)
#    print("gggggggg\n\n\n")
    return stems


def main():
 #   data = pd.read_csv('../wordslist.txt',names=['text'])
    data = pd.read_csv('../keywordslist.txt',names=['text'])  
    # text data in dataframe and removing stops words
    f = open('../outtfdf.txt')
    sw=[]
    while True:
        w = f.readline()
        if not w: break
        sw.append(w[:-1])

    stop_words = sw
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in stop_words]))
    
    # Using TFIDF vectorizer to convert convert words to Vector Space
    tfidf_vectorizer = TfidfVectorizer(max_features=200000,
                                       use_idf=True,
                                  #     stop_words='korean',
                                       tokenizer=tokenize_and_stem)
    
    # Fit the vectorizer to text data
 #   tfidf_matrix = tfidf_vectorizer.fit_transform(data['text'])
    
    tfidf_matrix = weighted_tfidf(data['text'])
    
    rows,cols=tfidf_matrix.nonzero()
  #  terms = tfidf_vectorizer.get_feature_names()
 #   print(tfidf_matrix.shape)

    # Kmeans++
 #   km = SpectralClustering(n_clusters=3,affinity="precomputed",n_neighbors=9)
    km = KMeans(n_clusters=15, init='k-means++', max_iter=10, n_init=1, verbose=0, random_state=3425)
    km.fit(tfidf_matrix)
    labels = km.labels_
    print(labels)
   # return

    clusters = labels.tolist()
    # Calculating the distance measure derived from cosine similarity
    distance = 1 - cosine_similarity(tfidf_matrix)

    # Dimensionality reduction using Multidimensional scaling (MDS)
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(distance)
    xs, ys = pos[:, 0], pos[:, 1]
    
    # Saving cluster visualization after mutidimensional scaling
    for x, y, in zip(xs, ys):
        plt.scatter(x, y)
    plt.title('MDS output of News Headlines')
    plt.savefig(os.path.join(path, 'results\MDS.png'))

    # Creating dataframe containing reduced dimensions, identified labels and text data for plotting KMeans output
    df = pd.DataFrame(dict(label=clusters, data=data['text'], x=xs, y=ys))
    df.to_csv(os.path.join(path, 'results\kmeans_clustered_DF.txt'), sep=',')

    label_color_map = {0: 'red',
                       1: 'blue',
                       2: 'green',
                       3: 'pink',
                       4: 'purple',
                       5: 'yellow',
                       6: 'orange',
                       7: 'grey',
                       8: 'black',
                       9: 'ivory',
                       10: 'pink',
                       11: 'black',
                       12: 'teal',
                       13: 'navy',
                       14: 'brown',
                       15: 'burgundy'
                       }

    csv = open(os.path.join(path, 'results\kmeans_clustered_output.txt'), 'w')
    csv.write('Cluster     Headline\n')

    fig, ax = plt.subplots(figsize=(9, 9))

    for index, row in df.iterrows():
        cluster = row['label']
        label_color = label_color_map[row['label']]
        label_text = row['data']
        ax.plot(row['x'], row['y'], marker='o', ms=12,c='white')
        row = str(cluster) + ',' + label_text + '\n'
        csv.write(row)

    # ax.legend(numpoints=1)
    for i in range(len(df)):
        ax.text(df.loc[i]['x'], df.loc[i]['y'], df.loc[i]['label'], size=8)

    plt.title('News Headlines using KMeans Clustering')
    plt.savefig(os.path.join(path, 'results\kmeans.png'))


if __name__ == '__main__':
    main()
