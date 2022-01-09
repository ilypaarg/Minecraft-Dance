import time
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyautogui as moose
import mouse as m

moose.FAILSAFE = False

right1 = 500
down1 = 0

left1 = -1000
down2 = 0

def sleep():
    time.sleep(0.5)

def rsleep():
    time.sleep(1)

def moosesleep():
    time.sleep(0.2)

def space():
    keyboard.press(Key.space)

def rspace():
    keyboard.release(Key.space)

def w():
    keyboard.press('w')

def rw():
    keyboard.release('w')

def a():
    keyboard.press('a')

def ra():
    keyboard.release('a')

def s():
    keyboard.press('s')

def rs():
    keyboard.release('s')

def d():
    keyboard.press('d')

def rd():
    keyboard.release('d')

def shift():
    keyboard.press(Key.shift)

def rshift():
    keyboard.release(Key.shift)

keyboard = Controller()

for dance in range(10):
    d()
    sleep()
    rd()
    sleep()
    d()
    sleep()
    rd()
    sleep()
    space()
    sleep()
    rspace()
    sleep()
    space()
    sleep()
    rspace()
    sleep()
    a()
    rsleep()
    ra()
    time.sleep(0.01)
    a()
    sleep()
    ra()
    a()
    sleep()
    ra()
    sleep()
    space()
    sleep()
    rspace()
    sleep()
    space()
    sleep()
    rspace()
    sleep()
    d()
    rsleep()
    rd()
    sleep()
    moose.click(1280, 720)
    sleep()
    moose.click(1280, 720)
    sleep()
    shift()
    sleep()
    rshift()
    sleep()
    shift() 
    sleep()
    rshift()
    sleep()
    moose.dragTo(2170, 729)
    sleep()
    moose.click(2170, 729)
    sleep()
    shift()
    sleep()
    rshift()
    sleep()
    moose.click(2170, 729)
    sleep()
    moose.dragTo(282, 711)
    sleep()
    shift()
    sleep()
    rshift()
    sleep()
    moose.click(282, 711)
    sleep()
    moose.click(282, 711)
