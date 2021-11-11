#!/usr/bin/env python3

import pyautogui
import time
import webbrowser
# Funcion creada con el propisito de mover a una coordenada y hacer click con el boton izquierdo


def MoverYHacerClick(posx, posy, click=1):
    pyautogui.moveTo(posx, posy)
    pyautogui.click()


# Usamos el modulo de webbrowser porque la funcion typewrite de pyautogui solo puede interpretar el teclado us
webbrowser.get(
    '/usr/bin/firefox').open_new("https://forms.office.com/r/S8Jy6Jsvmh")
# Usamos la funcion sleep para que no haga todo a la velocidad de la luz
time.sleep(5)

for i in range(2):
    # Preguntas
    # 1. Marvel o DC
    opc = str(input(
        "1. Marvel o DC\nA). Marvel\nB). DC\nC). Ambos\nD). Ninguno\nEscoga una opcion: "))
    if opc == "A":
        MoverYHacerClick(135, 505)
    elif opc == "B":
        MoverYHacerClick(135, 545)
    elif opc == "C":
        MoverYHacerClick(135, 585)
    elif opc == "D":
        MoverYHacerClick(135, 625)

    # Presionamos el boton "end" para irnos al final de la página
    pyautogui.press("end")

    # 2. Escribe un refrán, catchphrase, dicho popular o cita de libro o película
    opc = str(input(
        "2. Escribe un refrán, catchphrase, dicho popular o cita de libro o película: "))
    MoverYHacerClick(140, 425)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "x")
    pyautogui.typewrite(opc)

    # 3. Cuál es la mejor hora del día para comer pastel
    opc = str(input(
        "3. Cuál es la mejor hora del día para comer pastel\nA). 8 AM\nB). 9 AM\nC). 10 AM\n"
        "D). 11 AM\nE). 12 PM\nF). 1 PM\nG). 2 PM\nH). 3 PM.\nI). 4 PM\nJ). 5 PM\nK). 6 PM\n"
        "L). Después de las 7 PM\nEscoga una opcion: "))
    time.sleep(10)
    MoverYHacerClick(135, 585)
    time.sleep(5)
    if opc == "A":  # 8 AM
        MoverYHacerClick(135, 615)
    elif opc == "B":  # 9 AM
        MoverYHacerClick(135, 655)
    elif opc == "C":  # 10 AM
        MoverYHacerClick(135, 695)
    elif opc == "D":  # 11 AM
        MoverYHacerClick(135, 735)
    elif opc == "E":  # 12 PM
        MoverYHacerClick(135, 775)
    elif opc == "F":  # 1 PM
        MoverYHacerClick(135, 815)
    elif opc == "G":  # 2 PM
        MoverYHacerClick(135, 855)
    elif opc == "H":  # 3 PM
        MoverYHacerClick(135, 895)
    elif opc == "I":  # 4 PM
        MoverYHacerClick(465, 665)
        pyautogui.scroll(-80)
        time.sleep(5)
        MoverYHacerClick(135, 775)
    elif opc == "J":  # 5 PM
        MoverYHacerClick(465, 665)
        pyautogui.scroll(-80)
        time.sleep(5)
        MoverYHacerClick(135, 815)
    elif opc == "K":  # 6 PM
        MoverYHacerClick(465, 665)
        pyautogui.scroll(-80)
        time.sleep(5)
        MoverYHacerClick(135, 855)
    elif opc == "L":  # Después de las 7 PM
        MoverYHacerClick(465, 665)
        pyautogui.scroll(-80)
        time.sleep(5)
        MoverYHacerClick(135, 895)

    # 4. Ingresa una dirección de correo electrónico falsa
    opc = str(input("4. Ingresa una dirección de correo electrónico falsa: "))
    MoverYHacerClick(140, 725)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "x")
    pyautogui.typewrite(opc)

    if i == 0:
        # Enviar el formulario y  volver a hacer el otro formulario
        MoverYHacerClick(140, 825)
        time.sleep(15)
        MoverYHacerClick(135, 525)
        time.sleep(15)
        pyautogui.press("up")
    elif i == 1:
        # Cierra el navegador
        time.sleep(15)
        MoverYHacerClick(140, 825)
        time.sleep(5)
        pyautogui.hotkey("ctrl", "shift", "w")
