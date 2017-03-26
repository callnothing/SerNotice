from carriers.serverj import ServerJ
from carriers.email1 import Email
from settings import default
import sys

class Sender(object):


    @staticmethod
    def serverj_sender(title='', content=''):
        s = ServerJ(key=default['serverj_key'])
        s.send(title, content)

    @staticmethod
    def email_sender(title='', content=''):
        s = Email(**default)
        s.send(title, content)



def main():
    try:
        title = sys.argv[1]
        content = sys.argv[2]
    except:
        raise Exception("parms is incorrect")

    s = Sender()
    getattr(s, default.get('default_sender', 'serverj_sender'))(title, content)
