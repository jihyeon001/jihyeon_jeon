from sklearn import svm, metrics
import pandas

csv = pandas.read_csv("iris.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

print(data)
print(label)

clf = svm.SVC()     
clf.fit(data,label)

results = clf.predict([
    [5.1, 3.0, 1.3, 0.2]
])       
print(results)