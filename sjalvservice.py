import pyautogui
import time

time.sleep(5)  # Ge dig tid att öppna rätt fönster

antal_dagar = 6  # Ändra detta till hur många gånger du vill köra

for _ in range(antal_dagar):

    pyautogui.click(648, 327)  # Edit-knapp
    time.sleep(3)

    """In funktionen"""
    pyautogui.click(234, 276)  # Lägg till flex
    time.sleep(5)

    pyautogui.click(711, 331)   # klickar i inmatningfältet för tiden
    for _ in range(5):          # rensar tiden
        pyautogui.press('backspace')
        time.sleep(0.1)

    time.sleep(1)
    pyautogui.write("07")
    pyautogui.keyDown('shift')
    pyautogui.press('.')
    pyautogui.keyUp('shift')
    pyautogui.write("30")

    time.sleep(0.5)
    pyautogui.click(838, 386) # klickar på rullgardinen för typ
    time.sleep(1)
    # "pyautogui.click(875, 386) # in
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(927, 603)  # "lägg till"
    time.sleep(2)

    """Ut funktionen"""
    pyautogui.click(234, 276)  # Lägg till flex
    time.sleep(5)

    pyautogui.click(711, 331)   # klickar i inmatningfältet för tiden
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
    pyautogui.click(838, 386) # klickar på rullgardinen för typ
    time.sleep(1)
    #pyautogui.click(900, 386)  # "ut"
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)
    pyautogui.click(927, 603)  # "lägg till"
    time.sleep(2)

    pyautogui.click(1270, 622)  # Spara
    time.sleep(6)
    pyautogui.click(90, 223)   # Tillbaka
    time.sleep(5)
