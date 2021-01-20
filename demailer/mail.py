import email
from email.message import Message
from imaplib import IMAP4_SSL
from typing import Any, Generator, List, Tuple, Union

from demailer.config import config


def get_new_mail() -> Tuple[str, List[Any]]:
    conn = IMAP4_SSL(host=config.imap_host, port=config.imap_port)
    conn.login(user=config.imap_login, password=config.imap_password)

    conn.select()

    res = conn.search(None, "(NEW)")

    conn.close()
    conn.logout()

    return res


def get_messages(message_id_list: bytes) -> Generator[dict, None, None]:
    conn = IMAP4_SSL(host=config.imap_host, port=config.imap_port)
    conn.login(user=config.imap_login, password=config.imap_password)

    conn.select(readonly=True)

    for message_id in message_id_list.split(b" "):
        (_, raw_mail) = conn.fetch(message_id.decode("utf8"), "(RFC822)")

        parsed_mail = email.message_from_string(raw_mail[0][1].decode("utf8"))  # type: ignore

        sender_name, sender_address = email.utils.parseaddr(parsed_mail["from"])
        sender = (decode_utf8(sender_name), sender_address)

        recipients = []
        for recipient in parsed_mail["to"].split(","):
            name, address = email.utils.parseaddr(recipient)
            recipients.append((decode_utf8(name), address))

        subject = decode_utf8(parsed_mail["subject"])
        body = get_message_body(parsed_mail).decode("utf8")

        yield {"from": sender, "to": recipients, "subject": subject, "body": body}


def decode_utf8(raw: str) -> str:
    if raw:
        data, encoding = email.header.decode_header(raw)[0]
        if encoding:
            return data.decode(encoding)
        return data  # type: ignore
    return ""


def get_message_body(message: email.message.Message) -> bytes:
    if message.is_multipart():
        for part in message.get_payload():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True)
        return b""
    else:
        return message.get_payload(decode=True)
