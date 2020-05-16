import random
from random import randint

options = ["Piedra", "Papel", "Tijeras"]
print("Bienvenido al piedra, papel, tijera.")

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if(player == ai):
        return "Empate!"
    elif((player=='piedra' and ai == 'tijeras') or (player == 'tijeras' and ai == 'papel') or (player == 'papel' and ai == 'piedra')):
        return "Ganaste!"
    else:
        return "Perdiste!"

# Entry Point
def Game():
    try:
        condicion = False
        while condicion == False:
            opcion = int(input("Escoge una opción numérica: \n1-Piedra / 2-Papel / 3-Tijeras: "))
            if(opcion in (1,2,3)):
                    opcion = int(opcion) - 1
                    condicion = True
            else:
                print("Selección no válida, vuelve a intentarlo")

        ai = random.randint(0,2)
        print('La maquina escoge ' + options[ai])
        winner = quienGana(options[int(opcion)], options[ai])
        print(winner)
    except:
        print("Valor introducido no válido")
Game()
