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

The following examples use [HTTPie](https://github.com/jakubroztocil/httpie).

###Create a User

```shell
http --json POST http://localhost:8000/api/v1.0/users username=username password=password
```

###Authentication

```shell
http --json POST http://localhost:8000/api/v1.0/auth/token \
username=username password=password
# Authenticated requests use 'Authorization: Token'
http --json GET http://localhost:8000/api/v1.0/pages \
'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1'
```

###Create a Page

```shell
http --json POST http://localhost:8000/api/v1.0/pages \
    'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1' name=First
```

Adding a Stylesheet to a page
```shell
http -f PATCH http://localhost:8000/api/v1.0/pages/594d4ccb-a1bc-472b-b96f-48ed580bac9f \
'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1' stylesheet@stylesheet.css
```

Creating a Page with a stylesheet
```shell
http -f POST http://localhost:8000/api/v1.0/pages \
'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1' stylesheet@stylesheet.css name=Second
```

###Create Comments

```shell
http --json POST http://localhost:8000/api/v1.0/pages/594d4ccb-a1bc-472b-b96f-48ed580bac9f/comments \
'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1' text='Long Comment'
```

Reply Comment (using id from previous response)

```shell
http --json POST http://localhost:8000/api/v1.0/pages/594d4ccb-a1bc-472b-b96f-48ed580bac9f/comments \
'Authorization:Token bb83e4b5f137958432aacde8c64c6e99e11b1' text='Child Comment' parent=be347809-0dba-4e80-9646-0ba603408ddd
```

##Tests

```shell
coverage run --source='.' manage.py test
coverage html
firefox tmp/coverage/index.html
```
