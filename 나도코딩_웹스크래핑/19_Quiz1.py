from bs4  import BeautifulSoup
import requests

# Quiz 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오.
''' 
[조회조건]
1. http://daum.net 접속
2. '송파 헬리오시티' 검색
3. 다음 부동산 부분에 나오는 결과 정보

[출력 결과]
========= 매물 1 =========
거래: 매매
면적: 84/59 (공급/전용)
가격: 165,000 (만원)
동: 214동
층: 고/23
========= 매물 2 =========
. . .
'''

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

estate = soup.find("div", attrs={"id":"estateCollTabContents"})
estate_tbl = estate.find("tbody").find_all("tr")

# 나의 풀이
for i, estate in enumerate(estate_tbl):
    # lst = estate.find_all("td")
    lst = estate.get_text().split(" ")
    lst = list(filter(None, lst))
    print(f"========= 매물 {i+1} =========\n\
거래: {lst[0]}\n\
면적: {lst[1]} (공급/전용)\n\
가격: {lst[2]} (만원)\n\
동: {lst[3]}\n\
층: {lst[4]}")


# 강의 정답
for i, estate in enumerate(estate_tbl):
    lst = estate.find_all("td")
    
    print(f"========= 매물 {i+1} =========\n\
거래: {lst[0].get_text()}\n\
면적: {lst[1].get_text()} (공급/전용)\n\
가격: {lst[2].get_text()} (만원)\n\
동: {lst[3].get_text()}\n\
층: {lst[4].get_text()}")


# 참고
# 행 정보: tr
# tr 밑에 각 정보: td
# 모든 tr을 불러와 전체 행 정보를 저장하였고 for문 이용 각 행마다 정보를 출력
# 정보는 td 태그에 나눠져 있으므로 모든 td를 불러온 후 각 td별 텍스트 정보 출력
# 이 문제에선 td 정보가 5개 였지만 좀 더 정확하게 하려면 한줄 for 등을 사용하면 좋을 듯 함
# 12.csv_stock에서 한줄 for를 사용