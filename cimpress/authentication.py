import requests
import json
from .errors import CimpressError

def get_api_token(client_id, username, password):
    headers = {'Content-Type': 'application/json'}

    payload = {
        'client_id': client_id,
        'username': username,
        'password': password,
        'connection': 'default',
        'scope': 'openid email app_metadata',
    }

    response = requests.post("https://cimpress.auth0.com/oauth/ro",
                             data=json.dumps(payload),
                             headers=headers)

    if response.status_code != 200:
        raise CimpressError(response.json().get('error_description'))

    return response.json().get('id_token', None)
