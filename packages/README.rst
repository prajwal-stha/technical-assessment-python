=====
Users
=====

Users is a Django app to register users.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "users" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "users",
    ]

2. Include the users URLconf in your project urls.py like this::

    path("users/", include("users.urls")),

3. Run ``python manage.py migrate`` to create the users models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a user (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/users/ to register users.


Publish package
----------
1. ``python setup.py sdist``
2. ``python -m twine upload --repository testpypi dist/*``