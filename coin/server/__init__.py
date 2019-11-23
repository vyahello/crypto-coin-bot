from typing import Tuple
from coin.server.core import Server, WebServer
from coin.server.requests import Request, ServerRequest

coin_app: Server = WebServer()
WELCOME_MESSAGE: str = '<h1>Coin bot server powered by flask micro-web framework. Core is written by V.Yahello</h1>'
METHODS: Tuple[str, ...] = ('POST', 'GET')
POST = 'POST'

from . import routes
