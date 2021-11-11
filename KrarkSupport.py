# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:15:34 2021

@author: zaius
"""

class KrkAux:
    """
    Additional support cards for krark calculations
    """
    def __init__(self):
        pass
    
    def HarmProd(KrkNum, HarmNum):
        totalKrk = []
        totalHarm = []
        for each in KrkNum:
            totalKrk.append(1)
        for each in totalKrk:
            totalHarm.append(each + HarmNum)
        return sum(totalHarm)

    def Scoundrel(coin):
        return coin.count("Heads")*2
                
                