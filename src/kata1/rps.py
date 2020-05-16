import random 
from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if(player == ai):
        respuesta = 'Empate!'
    elif((player == 'tijeras' and ai == 'papel') or (player == 'papel' and ai == 'piedra') or (player == 'piedra' and ai == 'tijeras')):
        respuesta = 'Ganaste!'
    else:
        respuesta = 'Perdiste!'

    return respuesta

# Entry Point
def Game():
    #Se podría meter también en un try-except por si el valor introducido no es numérico, aunque en este caso no se usará
    try:
        #variable de condicion para el bucle
        seleccionValida = False
        #Se pregunta la elección hasta que se introduce un valor numérico válido
        while seleccionValida == False:
            seleccion = int(input("1-Piedra / 2-Papel / 3-Tijeras\nSelecciona una opción numérica: "))
            if(seleccion in (1,2,3)):
                seleccion = seleccion - 1
                seleccionValida = True
            else:
                print("Selección no válida, vuelve a intentarlo.\n")    

        #se define la variable que recogerá el random de la ia
        iaSeleccion = random.randint(0,2)

        seleccion = options[seleccion]
        iaSeleccion = options[iaSeleccion]

        #Se llama al método que devuelve quien gana
        winner = quienGana(seleccion, iaSeleccion)
        print("Has seleccionado: " + seleccion + "\nLa mágina ha seleccionado: " + iaSeleccion)
        print(winner)

    except:
        print("Valor introducido no válido")

Game()