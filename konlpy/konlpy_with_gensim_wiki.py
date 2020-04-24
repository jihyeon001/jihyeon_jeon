#나무 위키, 위키피디아의 파일을 다운 후
from konlpy.tag import Twitter
from gensim.models import word2vec

# 파일열기
readFp = codecs.open("wiki.txt", "r", encoding="utf-8")
wakati_file = "wiki.wakati"
writeFp = open(wakati_file, "w", encodin="utf-8")

#형태소 분석
twitter = Twitter()
i = 0
#텍스트 한 줄씩 처리하기
while True:
	line = readFp.readline()
	if not line: break
	if i % 20000 == 0:
		print("current - " + str(i))
	i += 1
	malist = twitter.pos(line, norm=True, stem=True)
	# 필요한 어구만 대상지정
	r = []
	for word in malist:
		#어미/조사/구두점 등은 제외
		if not word[1] in ["Josa", "Eomi", "Punctuation"]:
			writeFp.write(word[0] + " ")
writeFp.close()

data = word2vec.Text8Corpus("wiki.wakati")          
model = word2vec.Word2Vec(data, size=100)   # 단어 수치화 배열의 크기
model.save("wiki.model")           
