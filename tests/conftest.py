from typing import Tuple, Callable
import pytest
from _pytest.fixtures import SubRequest
from ccbot.crypto.coins import Coin, CryptoCoin
from ccbot.crypto.rates import CoinStock, CoinMarketCup

_coins: Tuple[str, ...] = ('bitcoin', 'litecoin', 'zcash', 'ethereum', 'ripple')


@pytest.fixture( params=_coins)
def coin_market_cup(request: SubRequest) -> CoinStock:
    return CoinMarketCup(request.param)


@pytest.fixture(scope='function')
def crypto_coin() -> Callable[[str], Coin]:

    def _crypto_coin(coin: str) -> Coin:
        return CryptoCoin(coin)

    return _crypto_coin
