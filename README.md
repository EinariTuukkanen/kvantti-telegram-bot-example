# kvantti-telegram-bot-example

Example Telegram bot made for an article published in Kvantti I/19.

## Requirements

Python (3.X preferred) and PIP.

## Install

```
$ pip install python-telegram-bot
```

Create your bot using [@BotFather](https://t.me/BotFather). Save the bot's token to an ENV variable with
```
$ export TG_TOKEN="yourtokenhere"
```

## Run

```
$ python bot.py
```

You may leave the script running for example by using `screen`.

```
$ screen -S tgbot
```

Run the script and exit by pressing `ctrl + a` then `d`.

Continue with
```
$ screen -dr tgbot
```
