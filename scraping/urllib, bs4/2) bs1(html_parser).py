from bs4 import BeautifulSoup        #라이브러리의 고유 import 방식
html="""
<html>
    <body>
        <div id="meigen">
            <h1> 위키북스 도서 </h1>
            <ul class="items art it book">
                <li> 유니티 게임이펙트 입문 </li>
                <li> 스위프트로 시작하는 아이폰 앱 교과서 </li>
                <li> 모던 웹사이트 디자인의 정석 </li>
            </ul>
        </div>
    </body>
</html>
"""

soup=BeautifulSoup(html,'html.parser')        # parser

header = soup.select_one("body > div > h1")   # CSS선택자 이용
list_items = soup.select("ul.items > li")    

print(header.string)
print(soup.select_one("ul").attrs)     #soup.select_one("ul")를 변수지정 해도됌

for li in list_items:
    print(li.string)