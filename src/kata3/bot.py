import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    mensaje = "Hola, Geeks"
    update.message.reply_text(mensaje)
    return mensaje

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    mensaje = "Ayudame!"
    update.message.reply_text(mensaje)
    return mensaje

def mayus(update, context):
    #context.args[1]
    mensaje = context.args[0]
    mensaje = mensaje.upper()
    update.message.reply_text(mensaje)
    return mensaje

def alreves(update, context):
    """Repite el mensaje del usuario."""
    #
    mensaje = context.args[0]
    txt = mensaje[::-1]
    update.message.reply_text(txt)
    print(txt)
    return "txt"

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("871576518:AAEL_8TH16g29zCn4kYheuQC3p089PwYobw", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    #
    #
    #

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("mayus", mayus))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CommandHandler(alreves))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
