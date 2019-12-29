from KingModBot import TW_Connect

# clrargs
import sys


def main():
    # Get the path to the secrets folder
    secrets_path = sys.argv[1]

    twitch_connection = TW_Connect(secrets_path)

    print(twitch_connection.hash_connection())
    print(twitch_connection.read_secrets())
