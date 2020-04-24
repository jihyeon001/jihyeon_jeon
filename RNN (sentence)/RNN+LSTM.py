import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activiation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

fp = codecs.open("./BEXX003.txt", "r", encoding="utf-16") # 파일 불러오기
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText() + " 
print("코퍼스의 길이: ", len(text))

# 문자를 하나하나 읽어들이고 ID 붙이기
chars = sorted(list(set(text)))                 # 파일에서 사용된 한글자한글자 분리
print('사용되고 있는 문자의 수: ', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))  # 문자 : ID (번호), 딕셔너리
indices_char = dict((i, c) for i, c in enumerate(chars))  # ID -> 문자

# 텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):     # step = 3, 세글자 다음부터 20글자까지 다음 리스트 원소
    sentences.append(text[i:i + maxlen])         # 20글자씩 잘라서 sentences
    next_chars.append(text[i + maxlen])          # 20글자 다음 한글자만 따로 모음 

print('학습할 구문의: ', len(sentences))
print('텍스트를 ID 벡터로 변환합니다...')
# .zeros(n) n개의 0으로 이루어진 리스트 생성, dtype=bool, ==> 0을 False로 변환
# .zeros(x,y,z) => 3차원 배열
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)  
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
#[i 몇번째문장인지, t 문장내부의 몇번째글자인지, 캐릭터(글자)를 값으로 변환]        
        X[i, t, char_indices[char]] = 1    # data가 지금 글자
    y[i, char_indices[next_chars[i]]] = 1  # label은 다음 글자

# 모델 구축 
print('모델을 구축합니다...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activiation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

# 후보를 배열에서 꺼내기
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# 학습시키고 텍스트 생성하기 반복
for iteration in range(1, 60):
    print()
    print('-' * 50)
    print('반복 = ', iteration)
    model.fit(X, y, batch_size=128, nb_epoch=1)
    # 임의의 시작 텍스트 선택
    start_index = random.randint(0, len(text) - maxlen - 1)   # maxlen만큼 뽑을거라 미리 빼줌
    # 다양한 다양성의 문장 생성
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('---다양성 = ', diversity)
        generated = ''
        sentence = text[start_index: start_index + maxlen]    # random 하게 maxlen만큼 뽑음
        generated += sentence                       # 뽑아낸 문장 생성 후 추가
        print('--- 시드 = "' + sentence + '"') 
        sys.stdout.write(generated)
        # 시드를 기반으로 텍스트 자동 생성
        for i in range(400):                           
            X = np.zeros((1, maxlen, len(chars)))   # 배열 초기화
            for t, char in enumerate(sentence):     # 3차원 배열(tensor) X 생성
                X[0, t, char_indices[char]] = 1
            #다음에 올 문자를 예측
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_chars = indices_char[next_index]   # 뽑아낸 문장 다음에 나올 글자 예측하여 하나씩 추가
            # 출력
            generated += next_char                 # generated에 한글자 추가 
            sentence = sentence[1: ] + next_chars  # 앞글자 지우고 다음 글자 넣어서 초기화 * 400번반복 => 새로운 문단 생성
            sys.stdout.write(next_chars)
            sys.stdout.flush()
        print()