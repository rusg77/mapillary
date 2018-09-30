# coding: utf-8
import os

host = os.environ.get('TEST_HOST') or 'http://localhost:5000'
api_base_url = '{}/api/v1'.format(host)
users_url = '{}/users'.format(api_base_url)

max_field_length = 255
