import environ


@environ.config(prefix="DEMAILER")
class Config:
    poll_interval = environ.var(default=30, converter=int)
    imap_host = environ.var()
    imap_port = environ.var(default=993, converter=int)
    imap_login = environ.var()
    imap_password = environ.var()
    tg_bot_token = environ.var()
    tg_user_id = environ.var(converter=int)


config = environ.to_config(Config)

sender_stop_list = ("user@example.com",)

recipient_stop_list = ("all_users@my_company.com",)

subject_stop_list = ("Best deals of the year!",)

body_stop_list = ("You are receiving this email because you have subscribed to",)
