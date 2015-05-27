#Agora API

##Features

- [x] Create Users
- [x] Create a Page
- [x] Upload a stylesheet for a Page
- [x] Access stylesheet for a Page
- [x] Add Comments to a Page
- [x] Add Comments to a Comment

##Development Setup

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements/development.txt
```

```shell
python manage.py migrate
# Create initial admin user
python manage.py createsuperuser
```

```shell
# Run the API
python manage.py runserver
```

The API is now available at [http://localhost:8000/api/v1.0/](http://localhost:8000/api/v1.0/)

##Usage

###Authentication

```shell
http --json POST http://localhost:8000/api/v1.0/auth/token \
username=username password=password
# Authenticated requests use 'Authorization: Token'
http --json GET http://localhost:8000/api/v1.0/credit-cards \
'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1'
```

##Tests

```shell
coverage run --source='.' manage.py test
coverage html
firefox tmp/coverage/index.html
```
