from KingModBot import TW_Connect, MongoDatabase

# clrargs
import sys


def main():
    # Get the path to the secrets folder
    secrets_path = sys.argv[1]
    twitch_connection = TW_Connect(secrets_path)
    # Hash connections/api tokens for printable views
    # Raw view will be on the self.client_id and self.token
    twitch_connection.hash_connection()

    db = MongoDatabase(secrets_path)
    db = db.connect()

    print(db.get_collection('twitchbot_test'))
    # db.create_collection('twitchbot_test')
