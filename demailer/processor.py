from email.utils import parseaddr

from demailer.config import (
    body_stop_list,
    recipient_stop_list,
    sender_stop_list,
    subject_stop_list,
)
from demailer.mail import get_messages, get_new_mail
from demailer.tg import send_message


def process_new_mail():
    (_, messages) = get_new_mail()
    if len(messages[0]) != 0:
        for message in get_messages(messages[0]):
            if not (
                filter_mail_from(message)
                or filter_mail_to(message)
                or filter_subject(message)
                or filter_body(message)
            ):
                notify(message)


def filter_mail_from(message):
    if message["from"][1] in sender_stop_list:
        return True


def filter_mail_to(message):
    for recipient in message["to"]:
        if recipient[1] in recipient_stop_list:
            return True


def filter_subject(message):
    for stop_words in subject_stop_list:
        if stop_words in message["subject"]:
            return True


def filter_body(message):
    for stop_words in body_stop_list:
        if stop_words in message["body"]:
            return True


def notify(message):
    sender = (
        f"{message['from'][0]} <{message['from'][1]}>"
        if message["from"][0]
        else message["from"][1]
    )
    recipients = []
    for recipient in message["to"]:
        if recipient[0]:
            recipients.append(f"{recipient[0]} <{recipient[1]}>")
        else:
            recipients.append(recipient[1])

    send_message(
        f"""
New mail!
    From: {sender}
    To: {", ".join(recipients)}
    Subject: {message["subject"]}
    Body: {message["body"]}"""
    )
