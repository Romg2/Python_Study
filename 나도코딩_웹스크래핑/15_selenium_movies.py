import requests
from bs4  import BeautifulSoup

# 구글 플레이 영화 url
url = "https://play.google.com/store/movies/top"

# 한글이 있으면 한글로 반환해달라 Accept-Language
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}

res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs= {"class":"ImZGtf mpg5gc"})

# with open("movie.html", "w", encoding="utf8") as f:
#    # f.write(res.text)
#    f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)