from abc import ABC, abstractmethod
from typing import Dict, Any
from ccbot.bot import BOT_API_TOKEN
from ccbot.crypto.coins import Coin
from ccbot.web_api.requests import Request, SafeBotRequest
from ccbot.web_api.responses import Response
from ccbot.web_api.urls import CommonUrl


class Message(ABC):
    """Abstraction for a message."""

    @abstractmethod
    def send(self) -> Dict[Any, Any]:
        pass


class BotMessage(Message):
    """A message of a bot."""

    def __init__(self, chat_id: int, coin: Coin) -> None:
        self._chat_id: int = chat_id
        self._coin: Coin = coin
        self._req: Request = SafeBotRequest(CommonUrl('https://api.telegram.org/bot', BOT_API_TOKEN, '/sendMessage'))

    def send(self) -> Response:
        return self._req.post({'chat_id': self._chat_id, 'text': f"{self._coin.name()} costs {self._coin.price()} usd"})
