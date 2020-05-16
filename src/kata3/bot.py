import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    return ""

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    return ""

def mayus(update, context):
        #
        return ""

def alreves(update, context):
    """Repite el mensaje del usuario."""
    #
    return ""

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = #

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    #
    #
    #

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
