from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if ai == "piedra" and player == "papel":
        return "Ganaste!"
    elif ai == "piedra" and player == "piedra":
        return "Empate!"
    elif ai == "piedra" and player == "tijeras":
        return "Perdiste!"
    elif ai == "papel" and player == "papel":
        return "Empate!"
    elif ai == "papel" and player == "piedra":
        return "Perdiste!"
    elif ai == "papel" and player == "tijeras":
        return "Ganaste!"
    elif ai == "tijeras" and player == "papel":
        return "Perdiste!"
    elif ai == "tijeras" and player == "piedra":
        return "Ganaste!"
    elif ai == "tijeras" and player == "tijeras":
        return "Empate!"


# Entry Point
def Game():
    #
    #
    print("Estás jugando a piedra, papel o tijeras.")
    player = input("Por favor, introduce cual de los 3 movimientos quieres hacer: ")
    player = player.lower()

    suerte = randint(0,2)
    ai = options[suerte]
    ai = ai.lower()

    #
    #
    winner = quienGana(player, ai)

    print(winner)

    return 0


Game()
