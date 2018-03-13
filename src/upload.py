import json
from urllib3.fields import RequestField
from urllib3.filepost import encode_multipart_formdata, choose_boundary


def encode_multipart_related(fields, boundary=None):
    if boundary is None:
        boundary = choose_boundary()

    body, _ = encode_multipart_formdata(fields, boundary)
    content_type = str('multipart/related; boundary=%s' % boundary)

    return body, content_type


def encode_media_related(metadata, media, media_content_type):
    rf1 = RequestField(
        name='Media Metadata',
        data=json.dumps(metadata),
        headers={'Content-Type': 'application/json; charset=UTF-8'},
    )
    rf2 = RequestField(
        name='Media Content',
        data=media,
        headers={'Content-Type': media_content_type},
    )
    return encode_multipart_related([rf1, rf2])


def build_metadata(path, description=None):
    import os
    import mimetypes

    name = os.path.basename(path)
    type = mimetypes.guess_type(path)[0]

    meta = {'name': name, 'mimeType': type}
    if description:
        meta['description'] = description
    return meta


def upload(session, path):
    base = 'https://www.googleapis.com/upload/drive/v3/files'

    metadata = build_metadata(path, 'cool upload file yo')
    body, content_type = encode_media_related(
        metadata,
        open(path, 'rb').read(),
        'text/plain; charset=UTF-8')

    p = {'uploadType': 'multipart'}
    session.post(url=base, data=body, params=p,
                 headers={'Content-Type': content_type})


if __name__ == '__main__':
    from DriveSession import DriveSession
    s = DriveSession()
    path = './../test/example.txt'
    upload(s, path)
