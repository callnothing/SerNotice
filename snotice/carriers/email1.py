
import smtplib
from email.mime.text import MIMEText

from snotice.carriers import Carrier


class Email(Carrier):

    def __init__(self, **kwargs):
        super(Email, self).__init__(**kwargs)
        self.smtp_host = kwargs.get('smtp_host')
        self.smtp_name = kwargs.get('smtp_name')
        self.smtp_passsword = kwargs.get('smtp_passsword')
        self.smtp_sender = kwargs.get('smtp_sender')
        self.admin_email = kwargs.get('admin_email')

    def sender(self):

        try:
            msg = MIMEText(self.content)
            msg['From'] = self.smtp_sender
            msg['To'] = self.admin_email
            msg['Subject'] = self.title

            server = smtplib.SMTP_SSL(self.smtp_host)
            server.login(self.smtp_name, self.smtp_passsword)
            server.sendmail(self.smtp_sender, self.admin_email, msg.as_string())
            server.quit()
        except Exception as e:
            raise e
