from bs4  import BeautifulSoup
import requests


# Quiz 웹 스크래핑을 이용하여 나만의 비서를 만드시오.
''' 
[조건]
1. 네이버에서 오늘 서울의 날씨정보 가져오기
2. 헤드라인 뉴스 3건 가져오기
3. IT 뉴스 3건 가져오기
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문 가져오기
'''

def weather_scrape():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "Accept-Language":"ko-KR,ko"
    }

    # 네이버: 분당 날씨 링크
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%84%EB%8B%B9+%EB%82%A0%EC%94%A8"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    weather = soup.find("div", attrs={"class":"weather_area _mainArea"})


    # 날씨 정보
    w1 = weather.find("div", attrs={"class":"main_info"})

    today_text = w1.find("p", attrs={"class":"cast_txt"}).get_text()
    today_temp = w1.find("p", attrs={"class":"info_temperature"}).get_text().strip().replace("도씨","")
    min_temp = w1.find("span", attrs={"class":"min"}).get_text()
    max_temp = w1.find("span", attrs={"class":"max"}).get_text()

    # 미세먼지 정보
    w2 = weather.find("div", attrs={"class":"sub_info"})

    dust_1 = w2.find_all("dd")[0].find("span", attrs={"class":"num"}).get_text()
    dust_2 = w2.find_all("dd")[1].find("span", attrs={"class":"num"}).get_text()

    # 강수 정보
    w3 = weather.find("div", attrs={"class":"table_info weekly _weeklyWeather"})

    rain_morning = w3.find_all("span", attrs={"class":"rain_rate"})[0].get_text().strip()
    rain_afternoon = w3.find_all("span", attrs={"class":"rain_rate"})[1].get_text().strip()


    print("[오늘의 날씨]")
    print(f"{today_text}")
    print(f"현재 {today_temp} (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전 {rain_morning} / 오후 {rain_afternoon}\n")
    print(f"미세먼지 {dust_1}\n초미세먼지 {dust_2}")

def head_news():
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Accept-Language":"ko-KR,ko"
        }

    # 네이버 뉴스
    url = "https://news.naver.com/"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    head_news = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)

    print("[헤드라인 뉴스]")
    for i, news in enumerate(head_news):
        news_info = news.find("a")
        print(str(i+1) + ".",  news_info.get_text().strip())
        print(" (링크 : {0}{1})".format(url, news_info["href"]))

def it_news():
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Accept-Language":"ko-KR,ko"
        }

    # 네이버 뉴스
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    head_news = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    print("[IT 뉴스]")
    for i, news in enumerate(head_news):
        news_info = news.find_all("dt")[1].find("a")
        print(str(i+1) + ".",  news_info.get_text().strip())
        print(" (링크 : {0}{1})".format(url, news_info["href"]))

weather_scrape()
head_news()
it_news()