from sklearn.cluster import KMeans
import numpy as np

X=[]
weights=[]
for x in range(-2,2):
    for y in range(-2,2):
        X+=[[x,y]]
        if x>0 and y>0:
            weights+=[5]
        else:
            weights+=[1]
X=np.array(X)
weights=np.array(weights)
kmeans=KMeans(n_clusters=2,random_state=0).fit(X,sample_weight=weights)
print(X)
print(weights)
print()
print(kmeans.cluster_centers_)
print(kmeans.labels_)
