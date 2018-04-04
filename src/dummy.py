

if __name__ == "__main__":
    from requests_oauthlib import OAuth2Session
    import credential as cred
    import json

    path = './../tokens.json'
    with open(path, 'r') as fp:
        token = json.load(fp)

    auto_refresh_extra = {
        'client_id': cred.CLIENT_ID,
        'client_secret': cred.CLIENT_SECRET
    }

    s = OAuth2Session(client_id=cred.CLIENT_ID,
                      auto_refresh_kwargs=auto_refresh_extra)
    s.refresh_token(cred.TOKEN_URI,
                    refresh_token=token['refresh_token'])

    print(s.token)

    from list import list_all_files

    q = {'fields': 'files(id,mimeType,name,parents)'}
    res = list_all_files(s, q)
    print(res.text)