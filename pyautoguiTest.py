import pyautogui
import time

openx = 772
openy = 1056

minx = 1743
miny = 23

loginx = 1141
loginy = 607

chemx = 347
chemy = 499

quizx = 206
quizy = 814

#'''
pyautogui.click(openx, openy)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 't')
time.sleep(0.5)
pyautogui.typewrite('c')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(loginx, loginy)
time.sleep(1)

#pyautogui.click(minx, miny)

for i in range(0, 4):
    pyautogui.press('down')
    time.sleep(0.2)
    
pyautogui.click(chemx, chemy)
time.sleep(1)
pyautogui.click(quizx, quizy)
time.sleep(1.5)
pyautogui.press('down')
    

'''
while True:
    print(pyautogui.position())
    time.sleep(0.5)

'''