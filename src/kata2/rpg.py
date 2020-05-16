#!/usr/bin/python

import random
import string
from random import choice

def RandomPasswordGenerator(passLen=10):
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    password = ""
    password = password.join([choice(valores) for i in range(passLen)])
    return password


RandomPasswordGenerator()