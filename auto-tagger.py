import pyautogui
import time


x = int(input("Enter number of participants in the group (including you)"))
time.sleep(5)
print('Open whatsapp chatbox')

pyautogui.hotkey('shift', '2')
# pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.3)

for _ in range(x-2):
    pyautogui.hotkey('shift', '2')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(0.3)
