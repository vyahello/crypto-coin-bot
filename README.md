[![Build Status](https://travis-ci.org/vyahello/crypto-coin-bot.svg?branch=master)](https://travis-ci.org/vyahello/crypto-coin-bot)
[![Forks](https://img.shields.io/github/forks/vyahello/crypto-coin-bot)](https://github.com/vyahello/crypto-coin-bot/network/members)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/crypto-coin-bot)](https://hitsofcode.com/view/github/vyahello/crypto-coin-bot)

# Crypto currency telegram bot
>Basic telegram bot powered by a webhook that helps you get latest USD exchange rates for all types of crypto currencies.
>
> Bot is called `FoxCoinBot` that served by [pythonanywhere.com](https://pythonanywhere.com) hosting, search for it in the telegram to allow it help you to get your desired coin. Enjoy it!

**Tools**
> - `python3.6.5`
> - `flask`
> - `pytest`
> - `pythonanywhere` hosting

## Usage
Run script from the root directory of the project:
```bash
~ python coin_bot.py
```

## Demo

![Screenshot](demo/coinbot.png)

## Developments notes

### Run tests
Run `pytest` from shell in the root directory of the repository to run `unittests`. 
It uses [pytest.ini](pytest.ini) config file as a setup.

Please open `test-report.html` file to obtain testing report.

### Release notes

* 0.2.0
    * Implement travis CI
* 0.1.0
    * First distribution of an app

### Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `Apache` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. run `pip install -r requirements.txt` to install all required python packages
4. run `pip install -r requirements-dev.txt` to install all required python packages
