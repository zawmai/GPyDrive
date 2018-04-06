import os
from DriveSession import DriveSession

class Context(object):
    """
    Context Class to maintain app states and initialize oauth session
    """

    def __init__(self):
        """ Constructs a new Context object for app

        :param token:
        """
        super(Context, self).__init__()
        self.session = None
        self.token = None

    @property
    def token(self):
        return self.__token_path

    @token.setter
    def token(self, path):
        """Need work"""

    @property
    def session(self):
        return self.__session

    def initialize(self):
        """Need work"""

        self.__initialize_session()

    def __initialize_session(self):
        """Need work"""
        pass

    def __initialize_file_hierarchy(self):
        """Need work"""
        pass


if __name__ == "__main__":
    c = Context()