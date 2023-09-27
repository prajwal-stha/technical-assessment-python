# User Profile

Awesome user profile with roles.

### Overview

---

User Profile is a powerful and flexible toolkit for building user profiles.

This Project uses a reusable app `custom-user-profile`, which consists of the core logic of our project. Full documentaion of the reusable app is [here](https://github.com/anjaan-g/custom-user-profile)

### Requirements

-   Python 3.7+
-   Django 4.2, 4.1, 4.0, 3.2

We highly recommend and only support the latest patch release of each Python and Django series.

### Installation

Install using `pip`...

```sh
$ pip install custom-user-profile
```

`custom-user-profile` uses `django-crispy-forms` and `crispy-bootstrap5` for forms and templates rendering and should be included in the `'INSTALLED_APPS'` settings along with `'users'` app.

```python
INSTALLED_APPS = [
    ...
    'users',
    'crispy_forms',
    'crispy_bootstrap5',
    ...
]
```

### Usage in the app

Let's take a quick example of using User-Profile to build a simple user profile.
Starup a new project like so...

```python
pip install django
pip install custom-user-profile
django-admin startproject example .
```
Inside the example `urls.py`, include `users.urls` as such:
```
urlpatterns = [
    path('users', include('users.urls', 'users')),
]
```

Run the runserver method with `python manage.py runserver` and goto `http:localhost:8000`
If you are not a registered user then register with the link in the navbar.

If the logged in user is admin, then he/she can list all users, view their details, edit their details, archive the users or permanently delete the users.
