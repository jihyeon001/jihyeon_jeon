from bs4 import BeautifulSoup
import urllib.request

# 기상청 일기예보 소스코드 URL
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnID-108"
request = urllib.request.urlopen(url)    #request로 불러오기
xml = request.read()                     # .read() 파일내용전체를 문자열로 반환

soup = BeautifulSoup(xml, "html.parser") #html과 비슷, .parser로 분석
seoul = soup.find_all("location")[0]
datas = seoul.find_all("data")

for item in datas:
   print(item.find("wf").text)