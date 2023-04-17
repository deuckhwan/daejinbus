from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip # pyperclip.copy('스타트코딩') pyperclip.hotkey("ctrl","v")

# 브라우저 꺼짐 방지
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
time.sleep(2)

# 네이버 로그인 창 아이디

id = driver.find_element(By.CSS_SELECTOR, ".link_login")
id.click()
time.sleep(2)

pyperclip.copy("parkduck71")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("PARKdeuckhwan71!")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

login_bnt = driver.find_element(By.CSS_SELECTOR, ".btn_login")
login_bnt.click()
time.sleep(2)

mail_url = "https://mail.naver.com/v2/folders/0/all"
driver.get(mail_url)
time.sleep(2)
