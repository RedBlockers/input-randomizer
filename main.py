import time

import keyboard
from pynput.mouse import Listener
import random

def choisir_action(actions):
    total_proba = sum(action['proba'] for action in actions)
    rand_num = random.randint(1, total_proba)
    proba_cumulative = 0
    for action in actions:
        proba_cumulative += action['proba']
        if rand_num <= proba_cumulative:
            return action

def on_click(x, y, button, pressed):
    if mode == '2':
        if pressed and str(button) == "Button.middle":
            for char in text:
                if char == '\\':
                    keyboard.press_and_release('enter')
                else:
                    keyboard.write(char)
                if char == ' ':
                    time.sleep(.5)
    elif mode == '1':
            if pressed and str(button) == "Button.right":
                action = choisir_action(actions)
                keyboard.press_and_release(action['touche'])
                print(f"pressed {action['touche']}")



mode = input('quel mode voulez-vous\n1-Random picker\n2-Text Writer')
text = input("Enter the text to type: ")

actions = []
active = True
while active:
    _input = input('touche,proba : exemple :&,30')
    if _input != ' ':
        actions.append({'touche': _input.split(',')[0], 'proba': float(_input.split(',')[1])})
    else:
        active = False

with Listener(on_click=on_click) as listener:
    listener.join()
