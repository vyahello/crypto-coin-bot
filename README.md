# Crypto currency telegram bot
Basic telegram bot powered by a webhook that helps you get latest USD exchange rates for all types of crypto currencies.
Bot is called `FoxCoinBot` that served by [pythonanywhere.com](https://pythonanywhere.com) hosting, search for it in the telegram to allow it help you to get your desired coin. Enjoy it!

## Run a coin bot
Run script from the root directory of the project:
```bash
~ python cnbot.py
```

## Demo
![Screenshot](bin/demo/coinbot.png)

## Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahelo@@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all required python packages

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.
