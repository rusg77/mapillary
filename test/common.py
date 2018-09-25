import requests

from test.config import users_url, api_base_url


def create_user(user_params):
    response = requests.post(users_url,
                             json=user_params,
                             headers={'Content-Type': 'application/json'})
    return response


def get_users():
    response = requests.get(users_url,
                            headers={'Content-Type': 'application/json'})
    return response


def clean_up_users():
    response = requests.post('{}/automation/clean_up_users'.format(api_base_url))
    return response
