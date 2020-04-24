from sklearn import svm, metrics
import glob, os.path, re, json

files = glob.glob("./image_text/lang/train/*.txt")    # 경로/*.txt  모든 txt파일 

train_data = []
train_label = []

for file_name in files:                # 각 파일 basename(경로를 제외한 파일명) 추출
    basename = os.path.basename(file_name)    # 레이블 구하기
    lang = basename.split("-")[0]     # 이름 중 공통되는 부분( - 를 기준) 분리
    file = open(file_name, "r", encoding="utf-8")    # 파일 내 텍스트 추출
    text = file.read()                                     # 텍스트 읽기
    text = text.lower()                                  # 소문자로 변환
    file.close()                                            
    code_a = ord("a")                                  # ord("문자") =>  ASCII로 반환
    code_z = ord("z")                             #반환된 숫자를 배열에 넣어 측정
    count = [0 for n in range(0, 26)]             # 0 26개
    for character in text:                        # 알파벳 출현 빈도
        code_current = ord(character)             # 현재의 문자
        if code_a <= code_current <= code_a:
            count[code_current - code_a] += 1      # ASCII에서 a가 제일 작은수
    total = sum(count)                                       # 정규화, 벡터값 (0~1 사이)
    count = list(map(lambda n: n / total, count))

    train_data.append(count)                               #리스트에 값을 추가
    train_label.append(lang)


files = glob.glob("./image_text/lang/test/*.txt")
test_data = []
test_label = []

for file_name in files:                
    basename = os.path.basename(file_name)
    lang = basename.split("-")[0]     
    file = open(file_name, "r", encoding="utf-8") 
    text = file.read()                            
    text = text.lower()                           
    file.close()                                            
    code_a = ord("a")                             
    code_z = ord("z")                             
    count = [0 for n in range(0, 26)]             
    for character in text:                        
        code_current = ord(character)            
        if code_a <= code_current <= code_a:
            count[code_current - code_a] += 1    
    total = sum(count)                           
    count = list(map(lambda n: n / total, count))

    test_data.append(count)                      
    test_label.append(lang)

clf = svm.SVC()                          
clf.fit(train_data, train_label)                     
predict = clf.predict(test_data)                  
score = metrics.accuracy_score(test_label, predict)    
print("정답률 :  ",  score) 

report = metrics.classification_report(test_label, predict)    # 분류 결과 성능표
print("score=", score)
print("--- report ---")
print(report)