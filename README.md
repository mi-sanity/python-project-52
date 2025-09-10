### Hexlet tests and linter status:
[![Actions Status](https://github.com/mi-sanity/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mi-sanity/python-project-52/actions)


### SonarQube status:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mi-sanity_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mi-sanity_python-project-52)


### Domain link:
https://task-manager-8d90.onrender.com


# Project "Task Manager"
**Task Manager** is a task management system. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.


### Installation
```pytnon
git clone git@github.com:mi-sanity/python-project-52.git
cd python-project-52

make install
make build
make start
```

*After 'make install' create .env file:*
```pytnon
DATABASE_URL=postgresql://{user}:{password}@{host}:{port}/{db}
SECRET_KEY=your-secret-key # Django will refuse to start if SECRET_KEY is not set
```

### Technologies used
- python "^3.13"
- uv "^0.7.4"
- django "^5.2.5"
- dj-database-url "^3.0.1"
- django-filter "^25.1"
- django-bootstrap5 "^25.2"
- python-dotenv "^1.1.1"
- gunicorn "^23.0.0"
- psycopg2-binary "^2.9.10"
- whitenoise "^6.9.0"
- rollbar "^1.3.0"
