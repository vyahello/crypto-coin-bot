from typing import Tuple
from ccbot.server.core import Server, WebServer
from ccbot.server.requests import Request, ServerRequest

SERVER: Server = WebServer()
WELCOME_MESSAGE: str = '<h1>Coin bot server powered by flask micro-web framework. Core is written by V.Yahello</h1>'
METHODS: Tuple[str, ...] = ('POST', 'GET')
POST = 'POST'

from . import routes
