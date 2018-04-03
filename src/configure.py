import configparser
import credential as c
import os
import pathlib
DEFAULT_PATH = './../configure.txt'
DEFAULT_MESSAGE = "Please enter {}: "


def prompt(message=DEFAULT_MESSAGE, target=None, default=None):
    response = input(message.format(target))
    if not response:
        return default
    else:
        return response


config = configparser.ConfigParser()

default = config['DEFAULT']
path = pathlib.Path(DEFAULT_PATH)
default['Path'] = str(path.resolve())

config['Credential'] = {}
cred = config['Credential']
cred['client_id'] = prompt(target='client_id', default=c.CLIENT_ID)
cred['client_secret'] = prompt(target='client_secret', default=c.CLIENT_SECRET)
cred['token_uri'] = "https://accounts.google.com/o/oauth2/token"
cred['redirect_uri'] = "urn:ietf:wg:oauth:2.0:oob"
cred['auth_uri'] = "https://accounts.google.com/o/oauth2/v2/auth"
cred['scope'] = "https://www.googleapis.com/auth/drive"

if os.path.exists(DEFAULT_PATH):
    print('Please remove the existing configure file.')
else:
    with open(default['Path'], 'w') as fp:
        config.write(fp)
