# Demailer: a simple email-to-telegram proxy

[[_TOC_]]

## Installation and usage

- First, get yourself a copy of [poetry](https://github.com/python-poetry/poetry)
- Then, run `poetry install`
- Setup environmental variables as follows:
    - `DEMAILER_POLL_INTERVAL`: how often will Demailer check for new mail in seconds (default: 30)
    - `DEMAILER_IMAP_HOST`: your mail server hostname
    - `DEMAILER_IMAP_PORT`: your mail server port (default: 993)
    - `DEMAILER_IMAP_LOGIN`: your mail server login
    - `DEMAILER_IMAP_PASSWORD`: your mail server password
    - `DEMAILER_TG_BOT_TOKEN`: your own [TG bot's token](https://core.telegram.org/bots#creating-a-new-bot)
    - `DEMAILER_TG_USER_ID`: your own TG chat ID (go get one from [@userinfobot](https://t.me/userinfobot))
- Setup stop phrases and addresses in [the config file](demailer/config.py)
- Run with `python runner.py`
- Enjoy the show!

## FAQ
**Q:** Will Demailer show all unread messages in my inbox on startup?

**A:** No! Demailer searches messages with `(NEW)` IMAP status – this returns only those messages that weren't received by any of the email clients beforehand. 

##
**Q:** Does Demailer mark my messages as read upon notifying?

**A:** Again, no chance! Demailer only removes the `(NEW)` status from the message, they will remain unread until you actually read them in your favourite email client.

## Dockerization

_coming soon!_
