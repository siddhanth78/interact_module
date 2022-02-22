import pyautogui
import time

openx = 772
openy = 1056

closex = 1902
closey = 17

select_all_x = 148
select_all_y = 237

markreadx = 463
markready = 243

linkx = 259
linky = 436


pyautogui.click(openx, openy)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 't')
time.sleep(0.5)
pyautogui.typewrite('gmail')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(linkx, linky)
time.sleep(2)
pyautogui.click(select_all_x, select_all_y)
time.sleep(1)
pyautogui.click(markreadx, markready)
time.sleep(1)
pyautogui.click(select_all_x, select_all_y)
time.sleep(1)
pyautogui.click(closex, closey)

'''
while True:
    print(pyautogui.position())
    time.sleep(0.5)

'''