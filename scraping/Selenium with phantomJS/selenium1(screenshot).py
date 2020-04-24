from selenium import webdriver
url = "http://www.naver.com/"

browser = webdriver.PhantomJS()   #PhantomJS 드라이버 추출
browser.implicitly_wait(3)        #3초 대기하기
                                                     
browser.get(url)                  #url get요청
browser.save_screenshot("website.png")    #화면 캡처 후 저장
browser.quit()                            #브라우저 종료