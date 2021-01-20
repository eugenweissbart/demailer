from telebot import TeleBot
from telebot.types import Message

from demailer.config import config

bot = TeleBot(config.tg_bot_token)


def send_message(message: str) -> Message:
    bot.send_message(config.tg_user_id, message)
