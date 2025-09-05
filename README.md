# README – Enkel tidsregistrering med PyAutoGUI (macOS)

Det här är ett **enkelt, hårdkodat klick-skript** för att registrera arbetstid. Det är byggt för **en specifik laptop/skärmupplösning** och **måste köras manuellt**. Om du vill använda det på en annan dator behöver du själv justera koordinaterna. **Använd på egen risk.**
Har du önskemål om tillägg i framtiden – säg till!

---

## Förutsättningar

* **macOS**
* **Python 3** (finns ofta förinstallerat som `python3`)
* **En kodredigerare** (t.ex. Visual Studio Code)

Ladda ner VS Code: [https://code.visualstudio.com](https://code.visualstudio.com)

> Alternativ: vilken editor som helst funkar (t.ex. PyCharm, Sublime, nano).

---

## Installation (macOS)

1. **Öppna Terminal**
   Spotlight → skriv “Terminal” → Enter

2. **Kontrollera Python**

   ```bash
   python3 --version
   ```

   Om kommandot inte hittas: installera Python 3 från [https://www.python.org/downloads/](https://www.python.org/downloads/)

3. **Skapa (valfritt) en virtuell miljö**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Installera PyAutoGUI**

   ```bash
   pip3 install pyautogui
   ```

   > PyAutoGUI hämtar automatiskt beroenden som Pillow.
   > Om du senare vill använda bildigenkänning (`locateOnScreen`) kan OpenCV göra det stabilare:

   ```bash
   pip3 install opencv-python
   ```

---

## macOS-behörigheter (viktigt)

För att skriptet ska kunna **klicka och skriva** åt dig behöver Terminal/VS Code få rättigheter:

1. **Systeminställningar → Integritet och säkerhet → Hjälpmedel (Accessibility)**

   * Lägg till **Terminal** (eller **iTerm**) och **Visual Studio Code**.
   * Bocka i tillåtelse.

2. Om du ska använda **`locateOnScreen`** (skärmbildssökning):
   **Integritet och säkerhet → Skärminspelning (Screen Recording)**

   * Lägg till **Terminal**/ **VS Code** och bocka i tillåtelse.

Starta om Terminal/VS Code efter att du ändrat rättigheter.

---

## Kör skriptet

1. Spara din fil, t.ex. `register_tid.py`.
2. Öppna rätt fönster i tidrapporteringssystemet.
3. Kör:

   ```bash
   python3 register_tid.py
   ```

> Skriptet väntar några sekunder i början så att du hinner fokusera rätt fönster.

---

## Konfiguration

Skriptet använder **hårdkodade koordinater** (x, y). Om UI\:t inte matchar din skärm behöver du:

* Flytta musen till en knapp/fält → notera koordinater (t.ex. via `pyautogui.position()` i en separat liten testfil).
* Uppdatera koordinaterna i skriptet.
* Justera eventuella `time.sleep(...)` om sidor/menyer laddar långsammare.

> Tips: Aktivera PyAutoGUI-failsafe så att du kan avbryta snabbt genom att dra musen till **övre vänstra hörnet**:
>
> ```python
> import pyautogui
> pyautogui.FAILSAFE = True
> ```

---

## Kända begränsningar

* **Skört**: minsta UI-ändring eller annan skärmupplösning kan bryta flödet.
* **Tidsstyrt**: använder `sleep` – om sidan laddar långsammare kan klick ske för tidigt.
* **Endast 1 maskin**: byggt för en specifik laptop.

Vill du ha något mer robust i framtiden, se Roadmap nedan.

---

## Felsökning

* “Inget händer”: kontrollera **Accessibility**-rättigheter.
* Klickar fel: justera koordinaterna, sänk/öka `sleep`, kontrollera att rätt fönster har fokus.
* “Module not found”: säkerställ att du kör i rätt miljö och att `pip3 install pyautogui` lyckades.

---

## Roadmap (efter tid)

1. **Automatisk inloggning**

   * Lägga till sekvens för att fylla i användarnamn/lösenord (om policy och säkerhet tillåter).
   * Bättre väntelogik (”vänta tills elementet finns”) i stället för fasta `sleep`.

2. **`locateOnScreen`**

   * Byt från hårdkodade koordinater till **bildigenkänning** (PyAutoGUI + ev. OpenCV) för att hitta knappar/menyer mer robust, även om fönstret flyttas lite.
   * Begränsa sökregioner för hastighet och lägg in fallback till koordinater vid behov.

> Om systemet är webbaserat kan vi på sikt byta till **Playwright/Selenium** för elementstyrning i stället för pixelklick – mycket stabilare över tid.

---

## Ansvarsfriskrivning

Detta är ett **enkelt exempel** avsett för **en specifik laptop**. Om du använder det på andra datorer måste du **själv justera** och testa noggrant. **All användning sker på egen risk.**
Hör av dig om du vill ha **förbättringar eller tillägg**.
