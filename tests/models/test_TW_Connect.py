from KingModBot import TW_Connect
from pathlib import Path

path = Path(__file__).parents[2]
path = str(path) + '\\secretsfortests.json'
twitch_connection = TW_Connect(path)


def test_hash():
    assert twitch_connection.hash_connection() == ['be4c517bf02cec201cbe7a1da7f18cd9d48cc8260764f5f3dafc06ccb026eec0ae07a418b45d54924df028f061c6a9c6bd0d3fdeadd6ac3284df05bd31aead56',
                                                   '7aa0e6e5bbf2361243a2d00dd345434afbbc27856fde47d58d55bafee421dde28aa474b1a27559395c6a037ecb7c937e04239aec613b3c66ac514ad719585059']


def test_readfile():
    assert str(twitch_connection.read_secrets(
    )) == "namespace(database_con=namespace(port='27017', server='localhost'), twitch_con=namespace(channel='', client_id='123gaierlk23@I#lkcm', nickname='', token='1245lilacmeriklasdf'))"


def test_client_id_upd():
    assert twitch_connection.client_id == '123gaierlk23@I#lkcm'


def test_token_upd():
    assert twitch_connection.token == '1245lilacmeriklasdf'
