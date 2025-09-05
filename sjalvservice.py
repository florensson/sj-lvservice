import pyautogui
import time

time.sleep(5)  # Ge dig tid att öppna rätt fönster

antal_dagar = 1  # Ändra detta till hur många gånger du vill köra

for _ in range(antal_dagar):
    
    pyautogui.click(873, 291)  # Edit-knapp
    time.sleep(3)

    """In funktionen"""
    pyautogui.click(480, 234)  # Lägg till flex
    time.sleep(5)

    pyautogui.click(806, 294)
    for _ in range(5):
        pyautogui.press('backspace')
        time.sleep(0.1)

    time.sleep(1)
    pyautogui.write("07")
    pyautogui.keyDown('shift')
    pyautogui.press('.')
    pyautogui.keyUp('shift')
    pyautogui.write("30")

    time.sleep(0.5)
    pyautogui.click(1063, 357)
    time.sleep(1)
    pyautogui.click(934, 373)  # "in"
    time.sleep(3)
    pyautogui.click(1029, 572)  # "lägg till"
    time.sleep(2)

    """Ut funktionen"""
    pyautogui.click(480, 234)
    time.sleep(5)

    pyautogui.click(806, 294)
    for _ in range(5):
        pyautogui.press('backspace')
        time.sleep(0.1)

    time.sleep(1)
    pyautogui.write("16")
    pyautogui.keyDown('shift')
    pyautogui.press('.')
    pyautogui.keyUp('shift')
    pyautogui.write("00")

    time.sleep(0.5)
    pyautogui.click(1063, 357)
    time.sleep(1)
    pyautogui.click(925, 396)  # "ut"
    time.sleep(1)
    pyautogui.click(1029, 572)
    time.sleep(2)

    pyautogui.click(1265, 587)  # Spara
    time.sleep(6)
    pyautogui.click(317, 187)   # Tillbaka
    time.sleep(5)
