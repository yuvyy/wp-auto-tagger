import pyautogui
import time


x = int(input("Enter number of participants in the group (including you): "))
print('Open whatsapp chatbox')
for i in range(5,0,-1):
    print('Tagging starting in: {} sec'.format(i))
    time.sleep(1)
    

pyautogui.hotkey('shift', '2')
# pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.3)

for _ in range(x-2):
    pyautogui.hotkey('shift', '2')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(0.3)

print("Tagging complete press enter to send the tagged message")
