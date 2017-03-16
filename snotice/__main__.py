from carriers.serverj import ServerJ
from settings import default
import sys

class Sender(object):


    @staticmethod
    def sender(title='', content=''):
        s = ServerJ(key=default['serverj_key'])
        s.send(title, content)


def main():
    try:
        title = sys.argv[1]
        content = sys.argv[2]
    except:
        raise Exception("parms is incorrect")
    s = Sender()
    s.sender(title, content)

