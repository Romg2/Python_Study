from selenium import webdriver
import time
import requests
from bs4  import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}


# 페이지 이동
browser.get(url)

# 지정한 위치로 스크롤 내리기 / 자바 명령어라고 함
# 모니터(해상도) 높이인 1600 위치로 스크롤내리기
# browser.execute_script("window.scrollTo(0,1600)")


# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


# 반복해서 가장 아래로 스크롤 내리기
interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 화면 가장 아래로 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
print("스크롤 완료")

# 스크롤 완료된 url 정보를 가져옴
soup = BeautifulSoup(browser.page_source, "lxml")

# 클래스를 2개 이상 가져올 때
# movies = soup.find_all("div", attrs= {"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div", attrs= {"class":"Vpfmgd"})

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})

    # 할인 후 가격
    discount_price = movie.find("span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    if original_price:
        original_price = original_price.get_text()
    else:
        original_price = discount_price


    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {discount_price}")
    print(f"링크 : https://play.google.com{link}")
    print("-" * 120)

browser.quit()