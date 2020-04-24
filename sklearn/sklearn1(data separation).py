from sklearn import svm, metrics
import pandas
from sklearn.model_selection import train_test_split

csv = pandas.read_csv("iris.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

# train과 test의 data, label을 각각 튜플로 선언
train_data, test_data, train_label, test_label =\
    train_test_split(data, label)

clf = svm.SVC()     
clf.fit(train_data, train_label)
results = clf.predict(test_data)       

score = metrics.accuracy_score(results, test_label) 
print("정답률: ", score)