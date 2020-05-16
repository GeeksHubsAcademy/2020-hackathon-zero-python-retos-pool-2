from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player.lower() == ai.lower():
        return "Empate!"
    elif player.lower()=="piedra":
        if ai.lower() == "papel":
            return "Perdiste!"
        else:
            return "Ganaste!"
    elif player.lower()=="papel":
        if ai.lower() == "piedra":
            return "Ganaste!"
        else:
            return "Perdiste!"
    elif player.lower()=="tijeras":
        if ai.lower() == "piedra":
            return "Perdiste!"
        else:
            return "Ganaste!"


# Entry Point
def Game():
    #
    x = 1
    print("Seleccione la opción que quieres jugar:")
    for i in options:  
        print(str(x) + ". " + i)
        x=x+1
    #
    opt = input("Opción: ")
    if int(opt) == 1 or int(opt) == 2 or int(opt) == 3:
        validacion = True
    else:
        validacion = False
    #
    #
    player = int(opt)
    ai = randint(0,2)
    if validacion:

        print("Opción elegida por tí: " + options[player-1])
        print("Opción elegida por la maquina: " + options[ai])
    
        winner = quienGana(options[player-1], options[ai])
        print(winner)
    else:
        print("Valor invalido, un saludo")

        
if __name__ == '__main__':
    Game()