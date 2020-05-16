#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #se le da a la contraseña un valor
    contraseña = string.ascii_letters + string.digits + string.punctuation
    #devuelve una cadena que junta cada uno de los valores de contraseña durante la longitud de passLen
    return ''.join(random.choice(contraseña) for i in range(passLen))

#si en el paréntesis no se incluye ningún valor, cogerá por defecto 10
print(RandomPasswordGenerator())