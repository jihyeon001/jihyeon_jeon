import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#데이터 읽어 들이기
mr = pd.read_csv("agaricus-lepiota.data", header=None) # 1열의 P가 독성정보

#데이터 내부의 기호를 숫자로 변환
label = []
data = []
attr_list = []                         #               index  row
for row_index, row in mr.iterrows():   #.iterrows()는 행번호와 행의값
    label.append(row.iloc[0])          # 첫번째 열만 label에 추가
    row_data = []
    for v in row.iloc[1:]:
        row_data.append(ord(v))     # 나머지 열의 정보는 숫자(ord)로 정리
    data.append(row_data)           #ix[] 대신 iloc[]메소드 사용


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