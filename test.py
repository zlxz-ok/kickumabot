#Aqui voy a hacer las pruebas para el main.py osea donde aprendo a hacer el bot
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#RGB DEL VERDE RGB:(129, 229, 125)
#POSICION DE LA BARRA:X: 1385 Y:  340 
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#while keyboard.is_pressed("q") == False:
    #if pyautogui.pixel(1385,340) [0] == 129:
        #click(1385,340)
        #X: 1385 Y:  340 RGB: (129, 229, 125)
w_press = False
inico = None
holaactive = False
while True:
    if keyboard.is_pressed("q"):
       break
    try:
       p = pyautogui.locateOnScreen("botsini/hola.png",confidence=0.8) != None
    except pyautogui.ImageNotFoundException:
       p = False
    if p:
       if w_press:
          keyboard.release("w")
          w_press = False
       if not holaactive:
         keyboard.press("s")
         time.sleep(1.5)
         keyboard.release("s")
         win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,961,813,0,0)
         holaactive = True
    else:
       holaactive = False
    try:
     if pyautogui.locateOnScreen("botsini/kick.png",confidence=0.8) != None:
       win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,961,813,0,0)
       click(961,813)
     if pyautogui.locateOnScreen("botsini/hola.png",confidence=0.8) != None:
        pass
    except pyautogui.ImageNotFoundException:
       if pyautogui.pixel(1385,340) [0] == 129:
           if w_press:
              keyboard.release("w")
              w_press = False
           click(1385,340)
           if inico is None:
            inico = time.time()
    if inico is not None and time.time() - inico >= 21:
              if not w_press:
                 keyboard.press("w")
                 w_press = True
              inico = None
    
    time.sleep(0.5)
