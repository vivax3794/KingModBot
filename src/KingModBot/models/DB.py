import json
from pathlib import Path
from pymongo import MongoClient

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


class MongoDatabase():
    """
    Instantiates the connection to the database.

    """

    def __init__(self, path_to_secrets):
        self.path_to_secrets = Path(path_to_secrets)

    def connect(self):
        self.read_secrets()
        client = MongoClient(self.server, self.port)
        db = client.test_database
        return db

    def read_secrets(self):
        with open((self.path_to_secrets.absolute()), "r") as json_data:
            data = json_data.read()
            x = json.loads(data, object_hook=lambda d: Namespace(**d))
            self.server = x.database_con.server
            self.port = int(x.database_con.port)
            return
