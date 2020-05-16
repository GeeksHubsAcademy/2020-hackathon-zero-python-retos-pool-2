from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == ai:
        return "Empate!"
    elif player==1:
        if ai == 2:
            return "Perdiste!"
        else:
            return "Ganaste!"
    elif player==2:
        if ai == 1:
            return "Perdiste!"
        else:
            return "Ganaste!"
    elif player==3:
        if ai == 1:
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
    ai = randint(1,3)
    print("Opción elegida por tí: " + options[player])
    print("Opción elegida por la maquina: " + options[ai])
    
    winner = quienGana(player, ai)

    print(winner)


Game()