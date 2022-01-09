import time
import random
from typing import Text
import colorama
from colorama import Fore, Style, init
import os
import ctypes
import keyboard
import json
import pynput
import array
from pynput import keyboard
from pynput.keyboard import Key, Controller
import animations


global avSleep # Use in sleep function
avSleep = 3


def title(string):
    # Declare a title change function
    ctypes.windll.kernel32.SetConsoleTitleW(string)

def clear():
    # Declare system clear screen function (windows)
    os.system('cls')

def console(command):
    # Declare any console command (easier than typing 'os.system(command)')
    os.system(command)

def Sleep(int):
    # Easier than typinng time.sleep
    time.sleep(int)

def countdown(t):
    # timer
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1

# Creating Arrays
interval = [1] # Probably wont be used, i havent decided yet
danceMoves = ['w', 'w', 'w', 'a', 'a', 'a', 's', 's', 's', 'd', 'd', 'd', Key.space, Key.space, Key.space, Key.shift, Key.shift, Key.shift]

timer = (random.choice(interval)) # Might not use this either, also havent decided.
random_press = (random.choice(danceMoves)) # Also probably wont use this

keyboard = Controller()

def tpye_string_with_delay(string):
    for char in string:
        keyboard.press(char)
        delay = random.uniform(1, 30)
        Sleep()

title("Dancy Dancy v1.0 - Coded by nugs")
animations.on_load()
time.sleep(avSleep)
clear()

print(Fore.LIGHTRED_EX + "I think it's time to dance...")
Sleep(avSleep)
clear()
countdown(int(10))
print(Fore.LIGHTCYAN_EX + """

██████╗░░█████╗░███╗░░██╗░█████╗░██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██║████╗░██║██╔════╝░
██║░░██║███████║██╔██╗██║██║░░╚═╝██║██╔██╗██║██║░░██╗░
██║░░██║██╔══██║██║╚████║██║░░██╗██║██║╚████║██║░░╚██╗
██████╔╝██║░░██║██║░╚███║╚█████╔╝██║██║░╚███║╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

""")

import dance.py

