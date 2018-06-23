from typing import Callable
import pytest
from ccbot.crypto.coins import Coin


@pytest.mark.parametrize('coin, coin_id, name, label', [
    ('bitcoin', 'bitcoin', 'Bitcoin', 'BTC'),
    ('litecoin', 'litecoin', 'Litecoin', 'LTC'),
    ('zcash', 'zcash', 'Zcash', 'ZEC'),
    ('ethereum', 'ethereum', 'Ethereum', 'ETH'),
    ('ripple', 'ripple', 'Ripple', 'XRP'),
])
def test_coin_records(crypto_coin: Callable[[str], Coin], coin: str, coin_id: str, name: str, label: str) -> None:
    assert crypto_coin(coin).id() == coin_id
    assert crypto_coin(coin).name() == name
    assert crypto_coin(coin).label() == label
