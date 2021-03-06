from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn. import model_selection, metrics
import json

max_words = 56681    #  입력단어수, word-dic.json파일
nb_classes = 6       # 5개의 카테고리
batch_size = 64
nb_epoch = 20

# MLP 모델 생성
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0,5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy'
        optimizer='adam',
        metrics=['accuracy'])
    return model
# 데이터 읽어 들이기 
data = json.load(open("./newstext/data-mini.json"))

X = data["X"]  # text data
Y = data["Y"]  # category data

# 학습하기
X_train, X_test, Y_train, Y_test = train_test_split(X,Y) 
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print(len(X_train),len(Y_train))

model = KerasClassifier(             # 분류기
    build_fn=build_model,            # 위에서 빌드한 mlp함수를 사용
    nb_epoch=nb_epoch,
    batch_size=batch_size)
model.fit(X_train, Y_train)          # fit으로 학습

# 예측하기
y = model.predict(X_test)            # 예측
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test,y)
print("정답률 = ", ac_score)
print("리포트 = \n", cl_report)
