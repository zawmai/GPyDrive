import configparser
import credential as c
import os
import pathlib
import constants.pathname as pathname
import constants.message as message


def prompt(directive=message.ENTER_PROMPT, target=None, default=None):
    response = input(directive.format(target))
    if not response:
        return default
    else:
        return response


def write_config_file(filepath=pathname.CONFIG_PATH):
    config = configparser.ConfigParser()

    default = config['DEFAULT']
    path = pathlib.Path(filepath)
    default['config_path'] = str(path.resolve())
    path = pathlib.Path(filepath)
    default['token_path'] = str(path.resolve())

    config['Credential'] = {}
    cred = config['Credential']
    cred['client_id'] = prompt(target='client_id', default=c.CLIENT_ID)
    cred['client_secret'] = prompt(target='client_secret',
                                   default=c.CLIENT_SECRET)

    if os.path.exists(filepath):
        print('Please remove the existing configure file.')
    else:
        with open(filepath, 'w') as fp:
            config.write(fp)
