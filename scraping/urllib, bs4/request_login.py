import requests
from bs4 import BeautifulSoup

session = requests.session()
#로그인
url = "https://smart.mbstar.co.kr/sfa/mn/login.crm" 
data = { "redirect": "",
    "p_svrtime": "04011815",
    "p_scheme": "https:",
    "seed:":"",
    "p_userId": "jhjeon",
    "p_userPw":"!Q2w3e4r5t"
}
response = session.post(url, data=data)
response.raise_for_status()

#페이지 내 정보가지고 오기
url = "https://smart.mbstar.co.kr/sfa/co/my/comy01.do"
response = session.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
text = soup.select_one(".table-responsive table").get_text()
print(text)