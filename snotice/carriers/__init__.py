

class Carrier(object):


    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')


    def sender(self):
        pass


    def send(self, title='', content=''):
        print "ready to send message %s" % title
        if not self.title:
            self.title = title
        if not self.content:
            self.content = content
        self.sender()


