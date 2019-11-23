from coin.bot.messages import Answer, BotAnswer, BotMessage
from coin.bot.text import Text, InputText
from coin.crypto.coins import Coin, CryptoCoin
from coin.server import coin_app, METHODS, Request, ServerRequest, POST, WELCOME_MESSAGE, Server

_server: Server = coin_app


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
