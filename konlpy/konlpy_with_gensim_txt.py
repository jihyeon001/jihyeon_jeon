import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

# bs4를 이용해 text 긁어 오기
fp = codecs.open("2BEXXX01.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text body")
text = body.getText()

# twitter 형태소 분석기이용, 글자를 분리하는 작업
twitter = Twitter()
lines = text.split("\r\n")
results = []
for line in lines:
	r = []
	malist = twitter.pos(line, norm=True, stem=True)
	for (word, pumsa) in malist:                                       # 튜플로 나옴 () 있없 같음
		if not pumsa in ["Josa", "Eomi", "Punctuation"]:       # "들 모두 제거
			r.append(word)
	results.append((" ".join(r)).strip())                            # 띄어쓰기하고 붙여서 추가
	
output = ( " ".join(results)).strip()                                        # wakati 같은 형태 완성
with open("toji.wakati", "w", encoding="utf-8") as fp:   # 파일 생성
	fp.write(output)                                                           

# 최종 모델로 저장
data = word2vec.LineSentence("tojij.wakati")                # 파일 불러오기
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("toji.model")                                                    # 대상객체, 매개 변수들

''' 
cmd창에서 사용법
>>>from gensim.models import word2vec
>>>model = word2vec.Word2Vec.load("toji.mode")           # model 대상 지정
>>>model.most_similar(positive=["왕자", "여성"], negative=["남성"])[0:3]
=> 왕녀......여왕......공주....

positive=["비교단어"]   - 같은 뜻 단어 찾기, 여러개 가능
negative=["비교단어"]    -   뜻이 다른 단어 찾기, 여러개 가능
[0:n]  -  0~n 번째 까지만 표기

2) 단어 수치화(벡터값) 배열 확인 
model["대상단어"]
=> 단어의 수치화된 배열이 나타남 
'''
