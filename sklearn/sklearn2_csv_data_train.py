from sklearn import model_selection, svm, metrics
import pandas

train_csv = pandas.read_csv("./image_text/mnist/train.csv", header = None) 
tk_csv = pandas.read_csv("./image_text/mnist/t10k.csv", header = None)  

def test(l): 					     #숫자를 바이너리로
    output = []
    for i in l:
        output.append(float(i) / 256)
    return output

train_csv_data = list(map(test, train_csv.iloc[:, 1:].values))  
tk_csv_data = list(map(test, tk_csv.iloc[:, 1:].values))  #강제 list화

# : 모든 row,  1: 첫번째 이후
#map(매개변수, ) 지정된 함수를 적용 시켜줌

train_csv_label = train_csv[0].values            #[0] 헤더 가져오기
tk_csv_label = tk_csv[0].values

clf = svm.SVC()                          
clf.fit(train_csv_data, train_csv_label)                     
predict = clf.predict(tk_csv_data)                  
score = metrics.accuracy_score(tk_csv_label, predict)    
print("정답률 :  ",  score)           
