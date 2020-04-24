from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np


#딥 러닝 - 레이어생성, numpy 배열이 필요
#데이터 가공 
csv = pd.read_csv("bmi.csv")

csv["weight"] /= 100      # 정규화 (0~1) 를위해 [<키> / 200, <몸무게> / 100]
csv["height"] /= 200

bmi_class = {              # numpy 배열로 만듦   
    "thin" : [1, 0, 0],
    "normal" : [0, 1, 0],
    "fat" : [0, 0, 1]
}
# 입력 data = x, 출력 lable = y
y = np.empty((20000, 3))    #numpy 배열 메소드(행, 열) ones, zeros, eye(단위행렬)
for i, v in enumerate(csv["label"]):
    y[i] = bmi_class[v]

x = csv[["weight", "height"]].values

x_train, y_train = x[1:15001], y[1:15001]                
x_test, y_test = x[15001:20001], y[15001:20001]

#모델 생성
model = Sequential()
#레이어 형성, keras doc 참고
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile("rmsprop", "categorical_crossentropy", metrics=['accuracy'])
#학습
model.fit(
    x_train, 
    y_train,
    batch_size=100, 
    nb_epoch=20,
    validation_split=0.1, 
    callback=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)   #학습 정확도 올리는 메소드

#정답률
score = model.evaluate(x_test, y_test)
print()
print("score loss:", score[0])
print("score accuracy:", score[1])   # metrics=['accuracy']의 값이 나옴
