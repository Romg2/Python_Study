from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window() # 창 최대화

# 네이버 항공권
url = "https://flight.naver.com/flights/"

browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27, 다음달 28일 선택
# element 27이 이번달, 다음달 2개 등이므로 index 로 구분하였기에 element"s" s 붙임
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

# 제주도 선택, 항공권 검색 클릭
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click() # 제주도 선택
browser.find_element_by_xpath("//*[@id='searchArea']/a").click() # 항공권검색 link_text 대신 xpath 사용

# 10초를 기다리는데 뒤 xpath 가 실행될 때 까지, LINK_TEXT 등도 가능함
try:
    # 첫 번째 결과 출력
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located( (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]") ))
    print(elem.text)
finally:
    browser.quit()