import pyautogui
import time

# 현재 모니터의 화면 크기(해상도) 출력
# print(pyautogui.size())
#
# # 마우스의 포지션 위치
# time.sleep(2)
# print(pyautogui.position())

# 마우스 해당 포지션 위치로 이동
# pyautogui.moveTo(520, 1054, 2) # 3번째 인자값은 2초의 딜레이
#
# # 마우스 클릭 속성
# pyautogui.click()
#
# time.sleep(2)
# pyautogui.rightClick()
#
# time.sleep(2)
# pyautogui.doubleClick()
#
# time.sleep(2 )
# pyautogui.click(clicks=4, interval=1.5) # 3번의 클릭 1초마 실행

# 마우스의 드레그 속성
# 1498,66 1354,72

pyautogui.moveTo(1498, 66, 2)
pyautogui.dragTo(1354, 72, 2)