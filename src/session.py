from requests_oauthlib import OAuth2Session
import constants.pathname as pathname
import constants.message as message
import constants.auth as auth
import configure
import configparser
import json
import os


def write_to_json(token, path):
    with open(path, 'w') as fp:
        json.dump(token, fp, indent=True)


def load_from_json(path):
    with open(path, 'r') as fp:
        data = json.load(fp)
        return data


class DriveSession(OAuth2Session):

    def __init__(self,
                 config_path=pathname.CONFIG_PATH,
                 token_path=pathname.TOKEN_PATH):
        self.__config_path = config_path
        self.__token_path = token_path
        self.__initialize_session()

    def __initialize_session(self):
        # write/init config file if not exists yet
        if not os.path.exists(self.__config_path):
            configure.write_config_file(filepath=self.__config_path)

        # get client id and secret from config file
        config_file = configparser.ConfigParser()
        config_file.read(self.__config_path)
        credential = config_file['Credential']
        client_id = credential['client_id']
        client_secret = credential['client_secret']

        # init Super OAuth2 session
        extra = {'client_id': client_id,
                 'client_secret': client_secret}

        def updater(token):
            write_to_json(token, self.__token_path)

        super(DriveSession, self).__init__(client_id=client_id,
                                           auto_refresh_kwargs=extra,
                                           token_updater=updater)

        # fetch access token from file, otherwise from server
        if not os.path.exists(self.__token_path):
            self.__init_without_existing_token(client_secret)
        else:
            self.__init_with_existing_token(client_secret)

    def __init_without_existing_token(self, secret):
        # Set addition parameters for OAuth2 protcols
        self.redirect_uri = auth.REDIRECT_URI
        self.scope = auth.SCOPE

        # Get Authorization Code
        auth_url, state = self.authorization_url(auth.AUTH_URI,
                                                 access_type='offline',
                                                 prompt='select_account')
        print(message.AUTH_URL_PROMPT.format(auth_url))
        authorization_code = input(message.AUTH_CODE_PROMPT)

        # Exchange authorization code for access and refresh Tokens

        token = self.fetch_token(token_url=auth.TOKEN_URI,
                                 client_secret=secret,
                                 code=authorization_code)
        write_to_json(token, path=self.__token_path)

    def __init_with_existing_token(self, secret):
        with open(self.__token_path, 'r') as fp:
            token = json.load(fp)
            self.refresh_token(auth.TOKEN_URI,
                               refresh_token=token['refresh_token'])


if __name__ == '__main__':
    s = DriveSession(pathname.CONFIG_PATH, pathname.TOKEN_PATH)
    from list import list_all_files

    q = {'fields': 'files(id,mimeType,name,parents)'}
    res = list_all_files(s, q)
    print(res.text)