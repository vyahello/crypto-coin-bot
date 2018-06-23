from abc import ABC, abstractmethod
from typing import Dict, Any, Callable
from ccbot.bot import BOT_API_TOKEN
from ccbot.crypto.coins import Coin
from ccbot.web_api.requests import Request, SafeBotRequest
from ccbot.web_api.responses import Response
from ccbot.web_api.urls import CommonUrl
from ccbot.server import requests


class Message(ABC):
    """Abstraction for a message."""

    @abstractmethod
    def send(self) -> Dict[Any, Any]:
        pass


class Answer(ABC):
    """Abstraction for a answer."""

    @abstractmethod
    def chat_id(self) -> int:
        pass

    @abstractmethod
    def message(self) -> str:
        pass


class BotMessage(Message):
    """A message of a bot."""

    def __init__(self, chat_id: int, coin: Coin) -> None:
        self._chat_id: int = chat_id
        self._coin: Coin = coin
        self._req: Request = SafeBotRequest(CommonUrl('https://api.telegram.org/bot', BOT_API_TOKEN, '/sendMessage'))

    def send(self) -> Response:
        return self._req.post({'chat_id': self._chat_id, 'text': f"{self._coin.name()} costs {self._coin.price()} usd"})


class BotAnswer(Answer):
    """An answer from a bot."""

    def __init__(self, request: requests.Request) -> None:

        def _req() -> Dict[Any, Any]:
            return request.dct().get('message')

        self._req: Callable[..., Dict[Any, Any]] = _req

    def chat_id(self) -> int:
        return self._req().get('chat').get('id')

    def message(self) -> str:
        return self._req().get('text')
