import pyautogui as pag
import time


minimize = pag.locateOnScreen("min.png", confidence = 0.9, grayscale=True)

pag.moveTo(minimize)
pag.click()

time.sleep(1)

open_chrome = pag.locateOnScreen("chrome_icon.png", confidence = 0.8, grayscale=True)

pag.moveTo(open_chrome)
pag.click(clicks = 2)
    
time.sleep(3)

pag.typewrite('gmail.com')
pag.press('enter')
time.sleep(2)

select_all = pag.locateOnScreen("checkbox.png", confidence=0.9, grayscale=True)

pag.moveTo(select_all)
pag.click()

mark_as_read = pag.locateOnScreen("mark_as_read.png", confidence=0.9, grayscale=True)

pag.moveTo(mark_as_read)
pag.click()

time.sleep(0.5)

pag.hotkey('ctrl', 'w')