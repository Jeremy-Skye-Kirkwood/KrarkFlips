#Generate coin flips for krark
from math import nan
import random

#import tkinter as tk
#from string import ascii_letters

#Define our 2 sided coin
coin = ["Heads","Tails"]
spacer = "..............."

print("Heads resolves the spell copy.\nTails puts it back in my hand.")
#Gather input on how many flips we're doing
while True:
    try:
        krkq = int(input("How many Krark flips? "))
        print(spacer)
    except ValueError:
        print("Value is nan, please enter a number!")
        continue
    else:
        print("Coin flips resolve\nfrom top to bottom")
        print(spacer)
        for each in range(krkq):
            print(coin[random.randint(0,1)])
        print(spacer)
        krkq2 = str(input("Flip again? (y/n) "))
        if krkq2 == "y":
            continue
        elif krkq2 == "n":
            break
        else:
            print("Please enter y or n!")

