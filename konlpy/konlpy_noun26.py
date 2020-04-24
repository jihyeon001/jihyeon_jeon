import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter          

file = codecs.open("2BEXXX01.txt", "r" encoding="utf-16")   # 파일 내용 객체화

soup = BeautifulSoup(file, "html.parser")    # parser 이용
body = soup.select_one("text > body")        # CSS선택자 이용 
text = body.getText()                        # text 가져오기



twitter = Twitter()
word_dic = {}                                # 언어의 빈출 횟수를 기록
lines = text.split("\r\n")    
for line in lines:                           # 한줄씩 분할된 lines를 반복분
    malist = twitter.pos(line)               # 한줄씩 읽어 들여 malist에 저장
    for taeso, pumsa in malist:              # 튜플자료형이 므로 나눠서 반복
        if pumsa == "Noun":                  
            if not (taeso in word_dic):      # 명사가 없으면   
                word_dic[taeso] = 0          # 태소엔 0개 추가
            word_dic[taeso] += 1             # 있으면 1개 추가
# 많이 사용된 명사 50개 출력            
keys = sorted(word_dic.items(), key=lambda  x:x[1], reverse=True)    
for word, count in keys[:50]:
    print("{0}({1})".format(word, count), end="")
print()
