# request로 소스코드 가져오기
import urllib.request
import urllib.parse     #'초콜릿' (한글을) 인코딩

api="https:// URL 입력    "
values = {
    "a" : "10",
    #....
}
params=urllib. parse.urlencode(values)
url = api + "?" + params

data=urllib.request.urlopen(url).read()  #소스코드를 긁어옴

text=data.decode("utf-8")     