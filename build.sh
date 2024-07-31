pip3 install gunicorn
pip3 install Django==5.0.3 pillow==10.2.0 pytz==2024.1 requests==2.31.0 sqlparse==0.4.4 tzdata==2024.1 urllib3==2.2.1 whitenoise==6.6.0
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
echo
echo yes
