from coin.server import coin_app


def _run_coin_bot() -> None:
    """Runs coin bot app."""
    coin_app.run(host="0.0.0.0", port=9999)


if __name__ == '__main__':
    _run_coin_bot()
