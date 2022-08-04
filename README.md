# Django Accounts Base

This is an example app module for Django projects, designed to handle common account actions. This version of accounts supplements the default Django user model in lieu for an AbstractUser using an email as the identifier. The Profiles model is blank but ready to accept new values for your projects needs.

Account actions include:
- Authentication (login/logout)
- Registration  
- Password Change
- Profiles



> NOTE: _project_name_ is used in the instructions and refers the the Main App for your project.

## Requirements
1. A new project.
2. No existing Users, including super users.
  - [Link](https://stackoverflow.com/questions/42150499/how-do-i-delete-db-sqlite3-in-django-1-9-to-start-from-scratch) to delete a test SQLite DB and start anew.
3. Python 3 (preferably in a [venv](https://stackoverflow.com/questions/43069780/how-to-create-virtual-env-with-python3) environment)
4. Built with Django 4.0 (unsure of compatibility with previous versions)

## Steps
Clone this repo into the base of your Django project

Next, rename the folder from 'django-accounts-example-app' to simply 'accounts'.

> Side note: It recommended to delete the .git folder from this repo. Nesting Git Repos can cause issues. [Explaination](https://github.com/swcarpentry/git-novice/issues/272).

### In _project_name_/settings.py
Add 'accounts' to INSTALLED_APPS:

```py
# project_name/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'accounts.apps.AccountsConfig',
]
```

Instruct Django to use the custom user model instead of the default one:
```py
# project_name/settings.py
AUTH_USER_MODEL = 'accounts.User'
```
### In _project_name_/urls.py
Ensure that the main url dispatcher is including the accounts app.
```py
from django.urls import path, include # include will need to be added.

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```
### In terminal
Migrate your accounts app:
```sh
$ python3 manage.py makemigrations accounts
$ python3 manage.py migrate
```
> For this command to work, you cannot have any Users already implemented. Refer to the link above to see how to reset a SQLite DB.

### Templates
Each template for the user models has had their base template removed to be compatible. It is recommended to add your base template to keep consistency between pages. The code extend the base template is included as comments in the templates.

### In other apps
There are a couple ways to refer to the new custom user model. The code below should work but [here](https://learndjango.com/tutorials/django-best-practices-referencing-user-model) are some other methods to consider.
```py
from django.contrib.auth import get_user_model
User = get_user_model()
```
