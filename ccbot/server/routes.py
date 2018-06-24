from ccbot.bot.messages import Answer, BotAnswer, BotMessage
from ccbot.bot.text import Text, InputText
from ccbot.crypto.coins import Coin, CryptoCoin
from ccbot.server import SERVER, METHODS, Request, ServerRequest, POST, WELCOME_MESSAGE, Server

_server: Server = SERVER


@_server.route('/', methods=METHODS)
def index():
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == POST:
        text: Text = InputText(answer.message())

        if text.match():
            coin: Coin = CryptoCoin(text.get_coin())
            BotMessage(answer.chat_id(), coin).send()

    return WELCOME_MESSAGE
