


from service import get_service

service = get_service()


def get_files():
    response = service.get("https://www.googleapis.com/drive/v3/files")
    return response


def get_drive_overview():
    response = service.get("https://www.googleapis.com/drive/v3/about")
    return response

if __name__ == "__main__":
    print(get_drive_overview())
    print(get_files())