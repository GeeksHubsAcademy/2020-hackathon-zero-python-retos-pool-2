#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    for i in range(passLen):
        if i == 0:
            contra = random.choice(caracteres)
        else:
            contra = contra + random.choice(caracteres)
    return contragit