from abc import ABC, abstractmethod
from typing import Callable
from coin.crypto.rates import CoinMarketCup


class Coin(ABC):
    """Abstraction of a crypto currency."""

    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def label(self) -> str:
        pass

    @abstractmethod
    def price(self) -> str:
        pass


class CryptoCoin(Coin):
    """Concrete crypto currency."""

    def __init__(self, coin: str) -> None:

        def _market_data(value: str) -> str:
            return CoinMarketCup(coin).coin_records().get(value)

        self._market_data: Callable[[str], str] = _market_data

    def id(self) -> str:
        return self._market_data('id')

    def name(self) -> str:
        return self._market_data('name')

    def label(self) -> str:
        return self._market_data('symbol')

    def price(self) -> str:
        return self._market_data('price_usd')
