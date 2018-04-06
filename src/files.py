"""
    List All Files' Requested Metadata
"""

def list_all_files(session, payload=None):
    base = 'https://www.googleapis.com/drive/v3/files'
    return session.get(url=base, params=payload)

if __name__ == '__main__':
    from session import DriveSession
    s = DriveSession()
    q={'fields': 'files(id,mimeType,name,parents)'}
    resp = list_all_files(s, q)
    print(resp.text)




