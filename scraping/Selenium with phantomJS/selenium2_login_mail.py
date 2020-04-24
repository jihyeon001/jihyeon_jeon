from selenium import webdriver
url = "https://nid.naver.com/nidlogin.login"

browser = webdriver.phantomjs()
browser.implicitly_wait(3)
browser.get(url)              #url 바로써도 가능

element_id = browser.find_element_by_id("id")   #by_id는 id를 찾아서 넣어줌
element_id.clear()                              #입력창 내용 지우기
element_id.send_keys("아이디")                   #내용을 전달하는 함수
element_pw = browser.find_element_by_id("pw")
element_pw.clear()
element_pw.send_keys("비밀번호")
browser.save_screenshot("website_b.png") 

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
					 #css 선택자이용
button.submit()      # type=submit이었어서 .submit을 하면 버튼을 누름

# 메일 
browser.get("http:            ")                 #메일페이지로 이동
browser.save_screenshot("파일이름.png")           #메일페이지 확인
titles = browser.find_elements_by_css_selector("            ")  
                                         #elements 복수 = 여러개 가져옴
for title in titles:
   print("-", title.text)                # .text 방식으로 print
browser.quit()