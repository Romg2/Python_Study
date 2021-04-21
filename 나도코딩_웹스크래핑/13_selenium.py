from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 검색 모듈

# 크롬버전에 맞는 크롬 드라이버가 반드시 존재해야함
browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

# 네이버 로그인 버튼 지정
elem = browser.find_element_by_class_name("link_login")
# elem.click(): 클릭
# browser.back(): 뒤로 가기
# browser.forward(): 앞으로 가기
# browser.refresh(): 새로고침

# 네이버 검색 버튼 지정
elem = browser.find_element_by_id("query")

# 키워드 입력
elem.send_keys("나도코딩")

# 엔터 누르기
elem.send_keys(Keys.ENTER)

# elements 모든 a tag 정보 가져옴
elem = browser.find_elements_by_tag_name("a")


# for e in elem:
#     e.get_attribute("href")

# 다음으로 전환
browser.get("http://daum.net")

# 다음 검색 버튼 지정
elem = browser.find_element_by_id("q")
# 키워드 입력
elem.send_keys("나도코딩")

# xpath 이용 클릭 - 검색 돋보기의 xpath 복사
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

browser.close() # 현재 탭만 닫기
browser.quit() # 모든 탭 닫기