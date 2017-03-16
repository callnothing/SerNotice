
import requests
from snotice.carriers import Carrier


class ServerJ(Carrier):


    def __init__(self, **kwargs):
        super(ServerJ, self).__init__(**kwargs)
        self.key = kwargs.get('key')


    def sender(self):
        if not self.key:
            raise Exception("serverj needs a key")

        try:
            r = requests.get("http://sc.ftqq.com/{key}.send?text={text}&desp={desp}".format(key=self.key, text=self.title, desp=self.content), timeout=30)
        except Exception as e:
            raise e
