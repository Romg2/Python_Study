# 모듈
import theater_module # 모듈의 class, function 등 사용 가능
import theater_module as mv # 별칭
from theater_module import * # 전체 가져와서 모듈명 안적고 함수 등 사용 가능
from theater_module import price, price_morning # 일부만
from theater_module import price_soldier as F1 # 함수에 별칭

# 패키지: 모듈의 집합
import travel.thailand # 패키지.모듈
# from travel.thailand import ThailandPackage as TP

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from 패키지 import * 하려면 all에 설정해라
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()


# 어디서 사용하는 모듈인지 확인
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# pip
# pipy 구글 검색 후 보면 패키지 있는거 확인 가능
# pip install beautifulsoup4
# pip install show beautifulsoup4
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random
print(dir())
print(dir(random))

# list of python module
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")    

print(os.listdir())

# time
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))


import datetime
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("알게 된지 100일은", today + td)

# Quiz
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건: 모듈 파일명은 byme.py
# 출력 예제
# 이 프로그램은 0000에 의해 만들어졌습니다.
# 유튜브: http://youtube.com
# 이메일: 0000@0000.com

import byme
byme.sign()