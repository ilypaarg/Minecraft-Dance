import time
import sys
import os
import random
import colorama
from colorama import Fore, Style

def on_load():
    version = 1.0
    load_string = "You are using v1.0 of Nuhgi's Minecraft Dance Sequence..."
    ls_len = len(load_string)
    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0

    while (counttime != 100):
        time.sleep(0.075)
        load_string_list = list(load_string)

        x = ord(load_string_list[i])
        y = 0

        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_string_list[i] = chr(y)

        res = ''
        for j in range(ls_len):
            res = res + load_string_list[j]

        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()

        load_string = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")
