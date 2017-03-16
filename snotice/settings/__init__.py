import os
from os.path import expanduser
import json

home = expanduser('~')

default_config_path = os.path.join(home ,'.snotice')

default = {}

if os.path.exists(default_config_path):
    with open(default_config_path, 'r') as filereader:
        default = json.loads(filereader.read())
else:
    print "config file not exists, please create one like below in your user home '/userhome/.snotice':"
    print """
    {
        "serverj_key": "xxx",
        "xxx": "xxx"
    }
    """
