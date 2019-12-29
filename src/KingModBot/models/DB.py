import json
from pathlib import Path

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


class MongoDatabase():
    def __init__(self, path_to_secrets):
        self.path_to_secrets = Path(path_to_secrets)

    def read_secrets(self):
        with open((self.path_to_secrets.absolute()), "r") as json_data:
            data = json_data.read()
            x = json.loads(data, object_hook=lambda d: Namespace(**d))
            self.server = x.database_con.server
            self.port = x.database_con.port
            return
