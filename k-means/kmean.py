from sklearn.cluster import KMeans
import random
import matplotlib.pyplot as plt
x = []
y = []

num = 10
for i in range(0,num):
    x.append(random.random() + 3)
    y.append(random.random()  + 4)
for i in range(0,num):
    x.append(random.random() * .5 - 3)
    y.append(random.random() * .5 + 4)

for i in range(0,num):
    x.append(random.random() * 2 + 5)
    y.append(random.random() * 2  -4)

kmeans = KMeans(n_clusters=3)

kmeans.fit(list(zip(x,y)))


plt.scatter(x,y, c=kmeans.labels_)
plt.show()
