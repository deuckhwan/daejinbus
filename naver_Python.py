from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True) #브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging']) #불필요한 메세지 제거
chrome_driver = ChromeDriverManager().install() # 크롬 브라우저 버즌 자동업데이트
driver = webdriver.Chrome(chrome_driver, options=options)
url = 'https://naver.com'
driver.get(url)
