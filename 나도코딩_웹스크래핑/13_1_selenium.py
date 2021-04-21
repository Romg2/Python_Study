from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")


# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
n_id = "내 아이디"
n_pw = "내 비밀번호"

browser.find_element_by_id("id").send_keys(n_id)
browser.find_element_by_id("pw").send_keys(n_pw)

time.sleep(3) # 3초 정도 쉬었다 작업

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 5. html 정보 출력
print(browser.page_source)

# 6. 브라우저 종료
browser.quit()