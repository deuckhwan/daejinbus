import pyautogui
import time

# print(f'{pyautogui.position()}')

img = pyautogui.screenshot('img.png', region=(862, 1043, 30, 30))
click = pyautogui.locateCenterOnScreen('img.png')
pyautogui.click(click)

time.sleep(2)
pyautogui.moveTo(1667, 45)

time.sleep(2)
pyautogui.moveTo(934, 273)
pyautogui.click()

time.sleep(2)
pyautogui.typewrite(['delete'])
pyautogui.moveTo(1044, 603)
pyautogui.click()

time.sleep(2)
pyautogui.moveTo(1589, 153)
pyautogui.click()

