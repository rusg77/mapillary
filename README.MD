# Mapillary app

App which allows to create and store users

## Running the app

### Docker

Requirements:
```
docker -v
Docker version 18.06.1-ce, build e68fc7a

docker-compose -v
docker-compose version 1.22.0, build f46880f
```

Run the app:

```
docker-compose up --build -d
```


Terminate the app:

```
docker-compose down
```

### Local development

Requirements:
```
python --version
Python 3.7.0

pip --version
pip 18.0

postgres --version
postgres (PostgreSQL) 10.3
```

You have to have a configured pg database. Default credentials ```postgresql://mapillary:mapillary@localhost:5432/mapillary```.
You can change the db settings by editing ```DevelopmentConfig.SQLALCHEMY_DATABASE_URI``` in ```config.py```

Install required packages:
```
pip install --no-cache-dir -r requirements.txt
```

Run db migrations:
```
flask db upgrade
```

Run the app:
```
python app.py
```

### Enjoy!
```
http://localhost:5000/
```

## Project structure

* `app` folder contains forms, models, routes and templates
* `migrations` folder contains migration scripts to set up database
* `test` folder contains:
    * `api` folder with API tests
    * `web` folder with web tests
        * `pages` folder with web pages locators and methods
    * `common.py` contains common API methods which are useful for tests
    * `config.py` config for tests
    * `conftest.py` contains common pytest fixtures
    * `data.py` contains data which is common for tests
* `app.py` init script for the app
* `config.py` contains configurations for docker and development environments


## API spec

### Get users
```
curl -X GET http://localhost:5000/api/v1/users
{
  "users": [
    {
      "address": "NY",
      "birthdate": "2018-09-23",
      "email": "tom@example.com",
      "username": "Tom Smith"
    }
  ]
}
```

### Create user
```
curl -X POST http://localhost:5000/api/v1/users -d '{"address": "NY", "birthdate": "2018-09-23", "email": "ts@example.com", "username": "Tom Smith"}' -H "Content-type: application/json"
{
  "user": {
    "address": "NY",
    "birthdate": "2018-09-23",
    "email": "ts@example.com",
    "username": "Tom Smith"
  }
}
```

Fields validation example:
```
curl -X POST http://localhost:5000/api/v1/users -d '{"address": "NY", "birthdate": "2018-09-23", "email": "ts@example.com", "username": "Tom Smith"}' -H "Content-type: application/json"
{
  "error": "Email is already in use"
}
```

### Clean up users (for automation)
```
curl -X POST http://localhost:5000/api/v1/automation/clean_up_users
{
  "success": true
}
```

## Web spec

### User's list
```http://localhost:5000/```

### Create user
```http://localhost:5000/create_user```


## Tests
### Requirements

```
pip install --no-cache-dir -r test_requirements.txt
```

```
chromedriver -v
ChromeDriver 2.42.591059 (a3d9684d10d61aa0c45f6723b327283be1ebaad8)
```

### Run the tests
```
pytest -v
```
```
test/api/test_create_user.py::TestCreateUser::test_create_user[simple_user-user0] PASSED                                                                                                                                                                                   [  3%]
test/api/test_create_user.py::TestCreateUser::test_create_user[cyrillic_user-user1] PASSED                                                                                                                                                                                 [  6%]
test/api/test_create_user.py::TestCreateUser::test_create_user[chinese_user-user2] PASSED                                                                                                                                                                                  [ 10%]
test/api/test_create_user.py::TestCreateUser::test_create_user[max_length_user-user3] PASSED                                                                                                                                                                               [ 13%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[username_is_empty_str-user_params0-Username is required] PASSED                                                                                                                                         [ 16%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[email_is_empty_str-user_params1-Email is required] PASSED                                                                                                                                               [ 20%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[birthdate_is_empty_str-user_params2-Birthdate is required] PASSED                                                                                                                                       [ 23%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[address_is_empty_str-user_params3-Address is required] PASSED                                                                                                                                           [ 26%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[username_is_empty_str-user_params4-Username is required] PASSED                                                                                                                                         [ 30%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[email_is_empty_str-user_params5-Email is required] PASSED                                                                                                                                               [ 33%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[birthdate_is_empty_str-user_params6-Birthdate is required] PASSED                                                                                                                                       [ 36%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[address_is_empty_str-user_params7-Address is required] PASSED                                                                                                                                           [ 40%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[username_is_too_long-user_params8-Username is too long] PASSED                                                                                                                                          [ 43%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[email_is_too_long-user_params9-Email is too long] PASSED                                                                                                                                                [ 46%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[birtdate_is_too_long-user_params10-Birthdate is too long] PASSED                                                                                                                                        [ 50%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[address_is_too_long-user_params11-Address is too long] PASSED                                                                                                                                           [ 53%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[email_is_invalid_1-user_params12-Email format is invalid] PASSED                                                                                                                                        [ 56%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[email_is_invalid_2-user_params13-Email format is invalid] PASSED                                                                                                                                        [ 60%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[email_is_invalid_3-user_params14-Email format is invalid] PASSED                                                                                                                                        [ 63%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[birthdate_is_invalid_1-user_params15-Incorrect birthdate format, use YYYY-MM-DD] PASSED                                                                                                                 [ 66%]
test/api/test_create_user.py::TestCreateUser::test_user_is_invalid[birthdate_is_invalid_2-user_params16-Incorrect birthdate format, use YYYY-MM-DD] PASSED                                                                                                                 [ 70%]
test/api/test_create_user.py::TestCreateUser::test_email_already_exists PASSED                                                                                                                                                                                             [ 73%]
test/api/test_get_users.py::TestGetUsers::test_get_users[no_user-create_users0] PASSED                                                                                                                                                                                     [ 76%]
test/api/test_get_users.py::TestGetUsers::test_get_users[simple_user-create_users1] PASSED                                                                                                                                                                                 [ 80%]
test/api/test_get_users.py::TestGetUsers::test_get_users[cyrillic_user-create_users2] PASSED                                                                                                                                                                               [ 83%]
test/api/test_get_users.py::TestGetUsers::test_get_users[chinese_user-create_users3] PASSED                                                                                                                                                                                [ 86%]
test/api/test_get_users.py::TestGetUsers::test_get_users[max_length_user-create_users4] PASSED                                                                                                                                                                             [ 90%]
test/api/test_get_users.py::TestGetUsers::test_get_users[multiple_users-create_users5] PASSED                                                                                                                                                                              [ 93%]
test/web/test_create_user.py::TestUsersList::test_user_list PASSED                                                                                                                                                                                                         [ 96%]
test/web/test_users_list.py::TestUsersList::test_user_list PASSED 
```
Default host is `http://localhost:5000`. In order to change the default host you can set `TEST_HOST` env variable.
