from time import sleep
from pynput.keyboard import Key,Controller
import pyautogui as pyg


keyboard = Controller()

def volUp():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volDown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def tabSwitch():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)


def deskWindow():
    keyboard.press(Key.cmd_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.cmd_l)


def deskScreen():
    keyboard.press(Key.cmd_l)
    keyboard.press("d")
    keyboard.release("d")
    keyboard.release(Key.cmd_l)


def closeWindow():
    pyg.keyDown("alt")
    pyg.press("f4")
    pyg.keyUp("alt")

def fullVolume():
    for i in range(50):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
