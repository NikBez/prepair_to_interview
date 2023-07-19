import email
import imaplib
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class MailClient:

    def __init__(self, login, password):
        self.mail_login = login
        self.main_password = password

    def send_mail(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.mail_login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.mail_login, self.main_password)
        ms.sendmail(self.mail_login, ms, msg.as_string())

        ms.quit()

    def recieve_mail(self, header=None):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.mail_login, self.main_password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    mail_client = MailClient(login, password)

    mail_client.send_mail(subject, recipients, message)
    mail_client.recieve_mail()
