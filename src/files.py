"""
    List All Files' Requested Metadata
"""

def list_all_files(session, payload=None):
    base = 'https://www.googleapis.com/drive/v3/files'
    return session.get(url=base, params=payload)

if __name__ == '__main__':
    from session import DriveSession
    s = DriveSession()
    fields = "files(id,mimeType,name,parents)"
    query1 = "name = 'tsujita.txt'"
    query2 = "trashed = false"
    payload = {'fields': fields,
               'q': query2}
    resp = list_all_files(s, payload)
    print(resp.text)




