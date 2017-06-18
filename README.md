# Django Practice

- Python 3.6.1

## Install

```
git clone git@github.com:lovenery/django-practice.git
cd django-practice
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
vim .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```