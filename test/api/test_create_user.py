import pytest

from test.config import max_field_length
from test.data import simple_user, cyrillic_user, chinese_user, valid_email, valid_birthdate, valid_address, \
    valid_username, max_length_user
from test.common import create_user, get_users


@pytest.mark.usefixtures('clean_up_users_fixture')
class TestCreateUser:

    @staticmethod
    def assert_error_response(response, expected_error):
        assert response.headers['Content-type'] == 'application/json'
        assert response.status_code == 400
        assert response.json() == {'error': expected_error}

    @pytest.mark.parametrize('test_name, user', [
        ('simple_user', simple_user),
        ('cyrillic_user', cyrillic_user),
        ('chinese_user', chinese_user),
        ('max_length_user', max_length_user),
    ])
    def test_create_user(self, test_name, user):
        response = create_user(user)
        assert response.headers['Content-type'] == 'application/json'
        assert response.status_code == 200
        assert response.json() == {'user': user}
        # check user by get users api method
        assert get_users().json()['users'] == [user]

    @pytest.mark.parametrize('test_name, user_params, expected_error', [
        # required filed is missed
        ('username_is_empty_str', {'email': valid_email,
                                   'birthdate': valid_birthdate,
                                   'address': valid_address}, 'Username is required'),
        ('email_is_empty_str', {'username': valid_username,
                                'birthdate': valid_birthdate,
                                'address': valid_address}, 'Email is required'),
        ('birthdate_is_empty_str', {'username': valid_username,
                                    'email': valid_email,
                                    'address': valid_address}, 'Birthdate is required'),
        ('address_is_empty_str', {'username': valid_username,
                                  'email': valid_email,
                                  'birthdate': valid_birthdate}, 'Address is required'),
        # required filed is empty str
        ('username_is_empty_str', {'username': '',
                                   'email': valid_email,
                                   'birthdate': valid_birthdate,
                                   'address': valid_address}, 'Username is required'),
        ('email_is_empty_str', {'username': valid_username,
                                'email': '',
                                'birthdate': valid_birthdate,
                                'address': valid_address}, 'Email is required'),
        ('birthdate_is_empty_str', {'username': valid_username,
                                    'email': valid_email,
                                    'birthdate': '',
                                    'address': valid_address}, 'Birthdate is required'),
        ('address_is_empty_str', {'username': valid_username,
                                  'email': valid_email,
                                  'birthdate': valid_birthdate,
                                  'address': ''}, 'Address is required'),
        # field is too long
        ('username_is_too_long', {'username': 'a' * (max_field_length + 1),
                                  'email': valid_email,
                                  'birthdate': valid_birthdate,
                                  'address': valid_address}, 'Username is too long'),
        ('email_is_too_long', {'username': valid_username,
                               'email': 'a' * (max_field_length + 1),
                               'birthdate': valid_birthdate,
                               'address': valid_address}, 'Email is too long'),
        ('birtdate_is_too_long', {'username': valid_username,
                                  'email': valid_email,
                                  'birthdate': 'a' * (max_field_length + 1),
                                  'address': valid_address}, 'Birthdate is too long'),
        ('address_is_too_long', {'username': valid_username,
                                 'email': valid_email,
                                 'birthdate': valid_birthdate,
                                 'address': 'a' * (max_field_length + 1)}, 'Address is too long'),
        # email is invalid
        ('email_is_invalid_1', {'username': valid_username,
                                'email': '@',
                                'birthdate': valid_birthdate,
                                'address': valid_address}, 'Email format is invalid'),
        ('email_is_invalid_2', {'username': valid_username,
                                'email': 'abc@',
                                'birthdate': valid_birthdate,
                                'address': valid_address}, 'Email format is invalid'),
        ('email_is_invalid_3', {'username': valid_username,
                                'email': 'abc@@test.com',
                                'birthdate': valid_birthdate,
                                'address': valid_address}, 'Email format is invalid'),
        # birthdate is invalid
        ('birthdate_is_invalid_1', {'username': valid_username,
                                    'email': valid_email,
                                    'birthdate': "23-09-2018",
                                    'address': valid_address}, 'Incorrect birthdate format, use YYYY-MM-DD'),

        ('birthdate_is_invalid_2', {'username': valid_username,
                                    'email': valid_email,
                                    'birthdate': "2018/09/23",
                                    'address': valid_address}, 'Incorrect birthdate format, use YYYY-MM-DD'),
    ])
    def test_user_is_invalid(self, test_name, user_params, expected_error):
        response = create_user(user_params)
        self.assert_error_response(response, expected_error)
        # check user wasn't created
        assert get_users().json()['users'] == []

    def test_email_already_exists(self):
        create_user(simple_user)
        response = create_user(simple_user)
        self.assert_error_response(response, 'Email is already in use')
        assert get_users().json()['users'] == [simple_user]
