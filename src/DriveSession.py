from requests_oauthlib import OAuth2Session
import credential as cred



class DriveSession(OAuth2Session):

    def __init__(self, client_id=cred.CLIENT_ID,
                 client_secret=cred.CLIENT_SECRET, scope=cred.SCOPE,
                 redirect_uri=cred.REDIRECT_URI, auth_uri=cred.AUTH_URI,
                 token_uri=cred.TOKEN_URI):
        super(DriveSession, self).__init__(client_id,
                               redirect_uri=redirect_uri,
                               scope=scope)

        # Get Authorization Code
        auth_url, state = self.authorization_url(auth_uri,
                                                 access_type='offline',
                                                 prompt='select_account')
        print('Please go to {} and authorize acess'.format(auth_url))
        authorization_code = input('Enter code: ')

        # Exchange authorization code for access and refresh Tokens
        self.fetch_token(token_uri,
                         code=authorization_code,
                         client_secret=client_secret)


if __name__ == '__main__':
    s = DriveSession()




