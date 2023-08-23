echo "BUILD START"
python3 -m pip install --upgrade pip
python3 -m pip install --no-cache-dir -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py collectstatic --noinput --clear
# gunicorn --config gunicorn-cfg.py core.wsgi
#python3 manage.py runserver
echo "BUILD END"
