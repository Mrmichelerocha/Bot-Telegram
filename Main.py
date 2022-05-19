import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Estágios
FIRST, SECOND, THIRD = range(3)
# Dados de retorno de chamada
PACKS, VIDEOS, END, CHAMADAS, PACK_D, PACK_S, VIDEOS_D, VIDEOS_S, CHAMADAS_H, CHAMADAS_P = range(10)


def start(update: Update, context: CallbackContext) -> int:
    """Enviar mensagem em `/start`."""
    # Pegue o usuário que enviou /start e registre seu nome
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Construir InlineKeyboard onde cada botão tem um texto exibido
    # e uma string como callback_data
    # O teclado é uma lista de linhas de botões, onde cada linha é por sua vez
    # uma lista (daí `[[...]]`)
    keyboard = [
        [
            InlineKeyboardButton("/", callback_data=str(PACKS)),
            InlineKeyboardButton(".", callback_data=str(VIDEOS)),
            InlineKeyboardButton(",", callback_data=str(CHAMADAS)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Enviar mensagem com texto e InlineKeyboard anexado
    update.message.reply_text("", reply_markup=reply_markup)
    # Diga ao ConversationHandler que estamos no estado `FIRST` agora
    return FIRST


def start_over(update: Update, context: CallbackContext) -> int:
    """Solicita o mesmo texto e teclado que `start`, mas não como uma nova mensagem"""
    # Obter CallbackQuery da Atualização
    query = update.callback_query
    # CallbackQueries precisa ser respondido, mesmo que nenhuma notificação ao usuário seja necessária
    # Alguns clientes podem ter problemas de outra forma. Veja https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("/", callback_data=str(PACKS)),
            InlineKeyboardButton(".", callback_data=str(VIDEOS)),
            InlineKeyboardButton(",", callback_data=str(CHAMADAS)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Em vez de enviar uma nova mensagem, edite a mensagem que
    # originou o CallbackQuery. Isso dá a sensação de um
    # menu interativo.
    query.edit_message_text(text="", reply_markup=reply_markup)
    return FIRST


def packs(update: Update, context: CallbackContext) -> int:
    """Mostrar nova escolha de botões"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("/", callback_data=str(PACK_D)),
            InlineKeyboardButton(".", callback_data=str(PACK_S)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return FIRST


def videos(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("/", callback_data=str(VIDEOS_D)),
            InlineKeyboardButton(".", callback_data=str(VIDEOS_S)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return FIRST


def chamada(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("/", callback_data=str(CHAMADAS_H)),
            InlineKeyboardButton(".", callback_data=str(CHAMADAS_P)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return FIRST

def packD(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(PACKS)),
            InlineKeyboardButton("É esse!", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return SECOND

  
def packS(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(PACKS)),
            InlineKeyboardButton("É esse!", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return FIRST


def videosD(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(PACKS)),
            InlineKeyboardButton("É esse!", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return SECOND


def videosS(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(PACKS)),
            InlineKeyboardButton("É esse!", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return SECOND

def chamadaH(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(PACKS)),
            InlineKeyboardButton("É esse!", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return SECOND


def chamadaP(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Voltar", callback_data=str(PACKS)),
            InlineKeyboardButton("É esse!", callback_data=str(END)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    return SECOND

  
def endend(update: Update, context: CallbackContext) -> int:
    """Mostrar nova escolha de botões"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Vou ver denovo", callback_data=str(PACKS)),
            InlineKeyboardButton("Vou embora", callback_data=str(VIDEOS)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return THIRD



def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Tchau BB 👋, volte sempre!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("token")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(packs, pattern='^' + str(PACKS) + '$'),
                CallbackQueryHandler(videos, pattern ='^' + str(VIDEOS) + '$'),
                CallbackQueryHandler(chamada, pattern ='^' + str(CHAMADAS) + '$'),
                CallbackQueryHandler(packD, pattern ='^' + str(PACK_D) + '$'),
                CallbackQueryHandler(packS, pattern ='^' + str(PACK_S) + '$'),
                CallbackQueryHandler(videosD, pattern ='^' + str(VIDEOS_D) + '$'),
                CallbackQueryHandler(videosS, pattern ='^' + str(VIDEOS_S) + '$'),
                CallbackQueryHandler(endend, pattern ='^' + str(END) + '$'),
                CallbackQueryHandler(chamadaH, pattern ='^' + str(CHAMADAS_H) + '$'),
                CallbackQueryHandler(chamadaP, pattern ='^' + str(CHAMADAS_P) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern ='^' + str(PACKS) + '$'),
                CallbackQueryHandler(endend, pattern ='^' + str(END) + '$'),
            ],
            THIRD: [ 
                CallbackQueryHandler(start_over, pattern ='^' + str(PACKS) + '$'),
                CallbackQueryHandler(end, pattern ='^' + str(VIDEOS) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Adicione ConversationHandler ao dispatcher que será usado para lidar com atualizações
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Execute o bot até pressionar Ctrl-C ou o processo receber SIGINT,
    # SIGTERM ou SIGABRT. Isso deve ser usado na maioria das vezes, uma vez que
    # start_polling() não é bloqueante e irá parar o bot normalmente.
    updater.idle()


if __name__ == '__main__':
    main()
