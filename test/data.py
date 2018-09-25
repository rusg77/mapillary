# coding: utf-8
from test.config import max_field_length

valid_email = 'test@test.com'
valid_birthdate = '2018-09-23'
valid_address = 'Moscow'
valid_username = 'John Smith'

simple_user = {'username': 'Tom Smith',
               'birthdate': '2018-09-23',
               'address': 'NY',
               'email': 'tom@example.com'}

cyrillic_user = {'username': 'Руслан Гусейнов',
                 'birthdate': '2018-09-23',
                 'address': 'Москва',
                 'email': 'test@test.com'}

chinese_user = {'username': '減筆字',
                'birthdate': '2018-09-23',
                'address': '簡筆字',
                'email': 'testchina@test.com'}

max_length_user = {'username': 'a' * max_field_length,
                   'birthdate': '2018-09-23',
                   'address': 'b' * max_field_length,
                   'email': '{}@test.com'.format('c' * (max_field_length - 9))}
