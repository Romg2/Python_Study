from selenium import webdriver


# selenium 을 공부하고 싶으면 구글에 selenium with python 검색
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")

browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window() # 창 최대화

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# headless 유의점: user-agent 확인 하면 headless가 붙어있어 접근 거부 당할 수 있음
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# 대체 방법: option에 user-agent 정보를 추가
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")