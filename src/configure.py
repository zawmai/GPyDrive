import configparser
import os
import pathlib
from constants.pathname import CONFIG_PATH
from constants.message import INVALID_INPUT, ENTER_PROMPT


def prompt(directive=ENTER_PROMPT, target=None, default=None):
    response = input(directive.format(target))
    if not response:
        return default
    else:
        return response


def write_config_file(filepath=CONFIG_PATH):
    config = configparser.ConfigParser()

    default = config['DEFAULT']
    path = pathlib.Path(filepath)
    default['config_path'] = str(path.resolve())
    path = pathlib.Path(filepath)
    default['token_path'] = str(path.resolve())

    config['Credential'] = {}
    cred = config['Credential']
    cred['client_id'] = \
        prompt(target='client_id',
               default=INVALID_INPUT.format('client_id'))
    cred['client_secret'] = \
        prompt(target='client_secret',
               default=INVALID_INPUT.format('client_secret'))

    if os.path.exists(filepath):
        print('Please remove the existing configure file.')
    else:
        with open(filepath, 'w') as fp:
            config.write(fp)
