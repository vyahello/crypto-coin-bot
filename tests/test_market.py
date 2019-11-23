from coin.crypto.rates import CoinStock

_records: int = 15


def test_coin_market_cup(coin_market_cup: CoinStock):
    assert len(coin_market_cup.coin_records()) == _records
