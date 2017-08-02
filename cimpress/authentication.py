import requests
import json


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

    return response.json().get('id_token', None)
