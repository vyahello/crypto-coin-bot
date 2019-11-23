from typing import Callable
import pytest
from coin.crypto.coins import Coin


@pytest.mark.parametrize('coin, coin_id', [
    ('bitcoin', 'bitcoin'),
    ('litecoin', 'litecoin'),
    ('zcash', 'zcash'),
    ('ethereum', 'ethereum'),
    ('ripple', 'ripple'),
])
def test_coin_id(crypto_coin: Callable[[str], Coin], coin: str, coin_id: str) -> None:
    assert crypto_coin(coin).id() == coin_id


@pytest.mark.parametrize('coin, name', [
    ('bitcoin', 'Bitcoin'),
    ('litecoin', 'Litecoin'),
    ('zcash', 'Zcash'),
    ('ethereum', 'Ethereum'),
    ('ripple', 'Ripple'),
])
def test_coin_name(crypto_coin: Callable[[str], Coin], coin: str, name: str) -> None:
    assert crypto_coin(coin).name() == name


@pytest.mark.parametrize('coin, label', [
    ('bitcoin', 'BTC'),
    ('litecoin', 'LTC'),
    ('zcash', 'ZEC'),
    ('ethereum', 'ETH'),
    ('ripple', 'XRP'),
])
def test_coin_label(crypto_coin: Callable[[str], Coin], coin: str, label: str) -> None:
    assert crypto_coin(coin).label() == label
