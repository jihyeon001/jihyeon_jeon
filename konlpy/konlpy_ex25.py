from konlpy.tag import Twitter  

twitter = Twitter()

print(twitter.morphs(""))               # 형태소를 잘라서 표기
print(twitter.nouns(""))                # 명사만 추출
print(twitter.pos("", norm=True, stem=True))  
# 단어를 모두 분리 후 형태소와 해당하는 품사를 표시
# norm - ㅋㅋ같은 글도 분류, stem - 나욬의 어근을 추출해서 나요로 변경
# 꼬꼬마 형태소 분석기는 더 세세하게 분류함