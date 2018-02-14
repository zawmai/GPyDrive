from requests_oauthlib import OAuth2Session
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import AuthorizedSession

CLIENT_ID = \
    "992274955769-udvho55sooiecrbu2ikcd6l8ajpv2jsn.apps.googleusercontent.com"
CLIENT_SECRET = "5NC4ncGEcu_g3Py4kesxwgTf"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
SCOPE = 'https://www.googleapis.com/auth/drive'
AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://accounts.google.com/o/oauth2/token"


def create_oauth2_session():
    oauth2_session = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    return oauth2_session


def get_authorization(oauth_session):
    auth_url, state = oauth_session.authorization_url(AUTHORIZATION_URL,
                                                access_type='offline',
                                                prompt='select_account')

    print('Please go to {} and authorize acess'.format(auth_url))
    authorization_code = input('Enter code: ')
    return authorization_code


def get_token_dict(session, authorization_code):
    token_dict = session.fetch_token(TOKEN_URL,
                                    code=authorization_code,
                                    client_secret=CLIENT_SECRET)
    return token_dict


def create_credential(access_token, refresh_token):
    cred = Credentials(access_token,
                       refresh_token=refresh_token,
                       token_uri=TOKEN_URL,
                       client_id=CLIENT_ID,
                       client_secret=CLIENT_SECRET)
    return cred


def get_authorized_session(credential):
    return AuthorizedSession(credential)


def get_service():
    session = create_oauth2_session()
    auth_code = get_authorization(session)
    token = get_token_dict(session, auth_code)

    if __name__ == "__main__":
        print("Access token: {}".format(token))
        print('Is Authorized?: {}'.format(
            'Yes' if session.authorized else 'No'))

    cred = create_credential(token['access_token'], token['refresh_token'])

    if __name__ == "__main__":
        print('Getting Credentials.....')

    authorized_session = get_authorized_session(cred)
    return authorized_session


if __name__ == "__main__":
    service = get_service()
    response = service.get("https://www.googleapis.com/drive/v3/files")
    print(response.text)

