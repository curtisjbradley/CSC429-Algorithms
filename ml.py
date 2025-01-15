from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

X = [] #Input Data
Y = [] #Is Iris-setosa?
with open('iris.data') as data:
    for l in data:
        d = []
        for a in l.strip().split(",")[:-1]:
            d.append(float(a)) 
        if d == []:
            continue
        X.append(d)
        Y.append(l.strip().split(",")[-1])

model = make_pipeline(MultinomialNB())
model.fit(X, Y)
new_iris = [[5.84, 3.05, 3.76, 1.2], #Average Data
        [5.0, 3.1, 1.5, 0.2], #Closeish to Setosa
        [7, 3, 1.5, 1.5] #Closeish to versicolor
        ] 

predictions = model.predict(new_iris)
print(predictions) 

