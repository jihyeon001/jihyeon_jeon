from sklearn import svm, metrics
import glob, os.path, re, json
import matplotlib.pyplot as plt
import pandas as pd

files = glob.glob("./book-mlearn-2-master/lang/train/*.txt")    # 경로/*.txt  모든 txt파일 

train_data = []
train_label = []

for file_name in files:                # 각 파일 basename(경로를 제외한 파일명) 추출
    basename = os.path.basename(file_name)
    lang = basename.split("_")[0]     # 이름 중 공통되는 부분( - 를 기준) 분리
    file = open(file_name, "r", encoding="utf-8")    # 파일 내 텍스트 추출
    text = file.read()                        # 텍스트 읽기
    text = text.lower()                       # 소문자로 변환
    file.close()                                            
    code_a = ord("a")                         # ord("문자") =>  ASCII로 반환
    code_z = ord("z")                         #반환된 숫자를 배열에 넣어 측정
    count = [0 for n in range(0, 26)]         # 0 26개
    for character in text:                    # 알파벳 출현 빈도
        code_current = ord(character)         # 현재의 문자
        if code_a <= code_current <= code_a:
            count[code_current - code_a] += 1 # ASCII에서 a가 제일 작은수
    total = sum(count)                        # 정규화, 벡터값 (0~1 사이)
    count = list(map(lambda n: n / total, count))

    train_data.append(count)                 #리스트에 값을 추가
    train_label.append(lang)

graph_dict = {}                            # 그래프 준비, 딕셔너리
for i in range (0, len(train_label)):
    label = train_label[i]
    data = train_data[i]
    if not (label in graph_dict):
        graph_dict[label] = data

asclist = [[chr(n) for n in range (97, 97 + 26)]]  # a~z 까지 리스트 만들기

df = pd.DataFrame(graph_dict, index=asclist)       # pd의 데이터프레임

#그래프 그리기
plt.style.use('ggplot')                               # 그래프 스타일
df.plot(kind="bar", subplots=True, ylim=(0, 0.15))    # 종류, 크기
plt.savefig("lang-plot.png")                          # 파일저장

#실행시 환경변수 설정  :   export MPLBACKEND="agg"
