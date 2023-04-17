from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
url = 'https://google.com'

driver.get(url)

time.sleep(1)
# 윈도우창 크게
driver.maximize_window()
#action = ActionChains(driver)

# Keys.CONTROL (새탭으로 새창을 가지고옴)
driver.find_element(By.CSS_SELECTOR, ".gLFyf").send_keys("파이썬"+ Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md").click()
driver.find_element(By.CSS_SELECTOR, "#")
time.sleep(1)

# 새창의 해당 창으로 이동 리스트 형태의 0.1.2 역순은 -1.-2
driver.switch_to.window(driver.window_handles[-1])

#driver.find_element(By.ID, "identifierId").send_keys("hwan71.dp@gmail.com")
