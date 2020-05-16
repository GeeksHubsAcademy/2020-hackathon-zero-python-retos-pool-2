from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    resultado=""

    if (player.lower() == ai.lower()):
        resultado = "Empate!"

    if ((player.lower() == "piedra") and (ai.lower() == "papel")):
        resultado = "Perdiste!"

    if ((player.lower() == "papel") and (ai.lower() == "tijeras")):
        resultado = "Perdiste!"

    if ((player.lower() == "tijeras") and (ai.lower() == "piedra")):
        resultado = "Perdiste!"

    
    if ((player.lower() == "piedra") and (ai.lower() == "tijeras")):
        resultado = "Ganaste!"

    if ((player.lower() == "papel") and (ai.lower() == "piedra")):
        resultado = "Ganaste!"

    if ((player.lower() == "tijeras") and (ai.lower() == "papel")):
        resultado = "Ganaste!"    
  
    return resultado

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

