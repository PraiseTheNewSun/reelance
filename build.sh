pip install gunicorn
pip install Django==5.0.3 
pip install pillow==10.2.0 
pip install pytz==2024.1 
pip install requests==2.31.0 
pip install sqlparse==0.4.4 
pip install tzdata==2024.1 
pip install urllib3==2.2.1 
pip install whitenoise==6.6.0
pip install psycopg
python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate
