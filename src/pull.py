from constants.rest import FILES_URL
import json



def pull_file_by_id(session, fid, path=None):
    fname = get_name_by_id(session, fid)
    resp = get_content_response_by_id(session, fid)
    wpath = path if path else fname
    with open(wpath, 'wb') as fp:
        for chunk in resp.iter_content():
            if chunk:
                fp.write(chunk)
        return fname


def get_name_by_id(session, fid):
    if session and fid:
        fields = {'fields': 'name'}
        resource_url = '/'.join([FILES_URL,fid])
        res = session.get(url=resource_url, params=fields)
        if res.status_code == 200:
            body = json.loads(res.text)
            return body['name']
        else:
            print('Failed request with status code {}'.format(res.status_code))
    else:
        print('Invalid Session or File ID')


def get_content_response_by_id(session, fid, is_stream=True):
    if session and fid:
        query = 'alt=media'
        resource_url = '/'.join([FILES_URL, fid])
        res = session.get(url=resource_url, params=query, stream=is_stream)
        return res
    else:
        print('Invalid Session or File ID')


def pull(session, path):
    pass


if __name__ == '__main__':
    from session import DriveSession
    from constants.message import KEY_VALUE_PAIR
    filedId = '17O6LRnYZm1pgP7BzyA6q7Zy6dfawbiA9'
    s = DriveSession()
    # resp = get_content_by_id(s, filedId)
    # print(resp.url)
    # print("-----------------------------------------------------")
    # for k, v in resp.headers.items():
    #     print(KEY_VALUE_PAIR.format(k, v))
    # print("-----------------------------------------------------")
    # print(resp.text)
    # print("-----------------------------------------------------")
    pull_file_by_id(s, filedId, path='./../yo.pdf')