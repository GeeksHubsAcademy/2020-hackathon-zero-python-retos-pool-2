#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    contraseña = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(contraseña) for i in range(passLen))

print(RandomPasswordGenerator(50))