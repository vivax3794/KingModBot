import hashlib
import json
import pathlib

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace


class TW_Connect():
    """
    Censored display of bot connection information
    Used for testing while on stream
    """

    def __init__(self, path_to_secrets):
        self.path_to_secrets = pathlib.Path(path_to_secrets)

    def hash_connection(self):
        # Handles the hashing of the connection information so that it is not identifiable in a print statement
        secrets = self.read_secrets()

        connection = []
        hash_client_id = hashlib.sha512(
            str(secrets.twitch_con.client_id).encode('utf-8'))
        connection.append(hash_client_id.hexdigest())
        hash_token = hashlib.sha512(
            str(secrets.twitch_con.token).encode('utf-8'))
        connection.append(hash_token.hexdigest())
        return connection

    def read_secrets(self):
        with open((self.path_to_secrets.absolute()), "r") as json_data:
            data = json_data.read()
            x = json.loads(data, object_hook=lambda d: Namespace(**d))
            self.client_id = x.twitch_con.client_id
            self.token = x.twitch_con.token
            return x
