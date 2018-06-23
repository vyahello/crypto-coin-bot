from abc import ABC, abstractmethod
from typing import Dict
from ccbot.web_api.requests import Request, SafeBotRequest
from ccbot.web_api.urls import CommonUrl


class CoinStock(ABC):
    """Abstraction of a crypto currency stock."""

    @abstractmethod
    def coin_records(self) -> Dict[str, str]:
        pass


class CoinMarketCup(CoinStock):
    """Coin market cup crypto currency stock."""

    def __init__(self, coin: str) -> None:
        self._req: Request = SafeBotRequest(CommonUrl('https://api.coinmarketcap.com/v1/ticker/', coin))

    def coin_records(self) -> Dict[str, str]:
        return self._req.get().json()[0]
