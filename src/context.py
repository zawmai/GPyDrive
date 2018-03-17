import os
from DriveSession import DriveSession

DEFAULT_TOKEN_PATH = './../tokens.json'


class Context(object):
    """
    Context Class to maintain app states and initialize oauth session
    """

    def __init__(self, token_path=DEFAULT_TOKEN_PATH):
        """Need work"""
        super(Context, self).__init__()
        self.session = None
        self.token_path = token_path

    @property
    def token_path(self):
        return self.__token_path

    @token_path.setter
    def token_path(self, path):
        """Need work"""


    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, s):
        """Need work"""
        if s is None:
            self.__initialize_session()

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