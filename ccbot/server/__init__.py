from typing import Tuple
from ccbot.bot.messages import Answer, BotAnswer, BotMessage
from ccbot.bot.text import Text, InputText
from ccbot.crypto.coins import Coin, CryptoCoin
from ccbot.server.core import Server, WebServer
from ccbot.server.requests import Request, ServerRequest

server: Server = WebServer()

_WELCOME: str = '<h1>Coin bot server powered by flask micro-web framework. Core is written by V.Yahello</h1>'
_METHODS: Tuple[str, ...] = ('POST', 'GET')
_POST = 'POST'


@server.route('/', methods=_METHODS)
def index():
    request: Request = ServerRequest()
    answer: Answer = BotAnswer(request)

    if request.method() == _POST:
        text: Text = InputText(answer.message())

        if text.match():
            coin: Coin = CryptoCoin(text.get_coin())
            BotMessage(answer.chat_id(), coin).send()

    return _WELCOME
