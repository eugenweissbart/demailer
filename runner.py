from datetime import timedelta

from timeloop import Timeloop

from demailer.config import config
from demailer.processor import process_new_mail

loop = Timeloop()
loop._add_job(process_new_mail, timedelta(seconds=config.poll_interval))

if __name__ == "__main__":
    loop.start(block=True)
