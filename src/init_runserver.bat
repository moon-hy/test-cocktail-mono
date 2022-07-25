@echo off
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py flush --no-input
echo from django.contrib.auth import get_user_model;User = get_user_model();User.objects.create_superuser('admin', '', 'qwer1234!@')|python manage.py shell
python ./init_db.py
python ./manage.py runserver 8181