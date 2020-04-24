import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#데이터 읽어 들이기
mr = pd.read_csv("agaricus-lepiota.data", header=None) # 1열의 P가 독성정보

#데이터 내부의 기호를 숫자로 변환, 단순 분류일때 !!
label = []
data = []
attr_list = []   
for row_index, row in mr.iterrows():
    label.append(row.iloc[0])
    exdata = []
    for col, v in enumerate(row.iloc[1:]):     
        if row_index == 0:
            attr = {"dic" : {}, "cnt" : 0 }
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        # 버섯의 특징 기호를 배열로
        d = [0]*12
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

#데이터 나누기  train_test_split()
data_train, data_test, label_train, label_test = train_test_split(data, label)

#학습
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

#데이터 예측
predict = clf.predict(data_test)

#결과 확인
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 = ", ac_score)
print("리포트 = ", cl_report)