from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager
# 브라 우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불 필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹 페이지 주소 이동
driver.implicitly_wait(3) # 웹 페이지 로딩의 3초 기다림
driver.maximize_window() # 웹 페이지 화면 최대화
url = "https://www.naver.com"
driver.get(url)



