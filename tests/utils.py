import os
from cimpress.authentication import get_api_token
from cimpress.client import Client
from cimpress.errors import CimpressError

def get_client_with_token():
    client_id = os.environ.get('CIMPRESS_CLIENT_ID')
    username = os.environ.get('CIMPRESS_USERNAME')
    password = os.environ.get('CIMPRESS_PASSWORD')

    token = get_api_token(client_id, username, password)

    if not token:
        raise CimpressError("Unable to generate token")

    return Client(token, 'sandbox')
