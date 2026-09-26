#Aqui voy a hacer las pruebas para el main.py osea donde aprendo a hacer el bot
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#RGB DEL VERDE RGB:(136, 228, 121)
#POSICION DE LA BARRA: X: 1384 Y:  298 
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed("q") == False:
    if pyautogui.pixel(1385,340) [0] == 129:
        click(1385,340)
        #X: 1385 Y:  340 RGB: (129, 229, 125)