#Generate coin flips for krark
#from math import nan
import random
from KrarkSupport import KrkAux
#import tkinter as tk
#from string import ascii_letters

#Define our 2 sided coin
coin = ["Heads","Tails"]
spacer = "..............."
result = []
birgiMana = 0

print("Heads resolves the spell copy.\nTails puts it back in my hand.")

#Gather input on board variables
while True:
    try:
        krkq = range(int(input("How many Krarks? ")))
        krkq2 = int(input("How many Harmonic Prodigies? "))
        krkq3 = input("Do you have a Birgi? ")
        krkq4 = input("Do you have a Scoundrel? ")
        print(spacer)
    except ValueError:
        print("Value is nan, please enter a number!")
        continue
    else:
        print("Coin flips resolve\nfrom top to bottom")
        print(spacer)
        
        totalFlips = KrkAux.HarmProd(krkq,krkq2)
        
        for each in range(totalFlips):
            result.append(coin[random.randint(0,1)])
        print(*result, sep = "\n")
        
        if krkq3.lower() == "y":
            birgiMana += 1
            print(f'Red Mana = {birgiMana}')
        else:
            birgiMana = 0

        if krkq4.lower() == "y":
            print(f'Treasures = {KrkAux.Scoundrel(result)}')
        
        print(spacer)
        
        krkq2 = str(input("Flip again? (y/n) "))
        if krkq2 == "y":
            result.clear()
            continue
        elif krkq2 == "n":
            break
        else:
            print("Please enter y or n!")

