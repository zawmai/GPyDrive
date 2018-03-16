from requests_oauthlib import OAuth2Session
import credential as cred
import os
import json


TOKEN_PATH = './../tokens.json'


def write_to_json(token, path):
    with open(path, 'w') as fp:
        json.dump(token, fp, indent=True)


def load_from_json(path):
    with open(path, 'r') as fp:
        token = json.load(fp)
        return token


def drive_token_updater(token, path=TOKEN_PATH):
        write_to_json(token, path)


class DriveSession(OAuth2Session):

    def __init__(self,
                 client_id=cred.CLIENT_ID,
                 client_secret=cred.CLIENT_SECRET,
                 scope=cred.SCOPE,
                 redirect_uri=cred.REDIRECT_URI,
                 auth_uri=cred.AUTH_URI,
                 token_uri=cred.TOKEN_URI,
                 token_updater=drive_token_updater):

        refresh_extra = {'client_id': client_id,
                        'client_secret': client_secret}

        super(DriveSession, self).__init__(client_id,
                                           redirect_uri=redirect_uri,
                                           scope=scope,
                                           token_updater=token_updater,
                                           auto_refresh_kwargs=refresh_extra)

        # Get Authorization Code
        auth_url, state = self.authorization_url(auth_uri,
                                                 access_type='offline',
                                                 prompt='select_account')
        print('Please go to {} and authorize acesss'.format(auth_url))
        authorization_code = input('Enter code: ')

        # Exchange authorization code for access and refresh Tokens
        token = self.fetch_token(token_uri,
                         code=authorization_code,
                         client_secret=client_secret)
        write_to_json(token, TOKEN_PATH)


if __name__ == '__main__':
    s = DriveSession()
    token = s.refresh_token(cred.TOKEN_URI)
    print(token)
    print("access token: {}".format(token['access_token']))
    print("refresh token: {}".format(token['refresh_token']))
    token = s.refresh_token(cred.TOKEN_URI)
    print(token)
    print("access token: {}".format(token['access_token']))
    print("refresh token: {}".format(token['refresh_token']))




