echo "BUILD START"
python3.9 -m pip install --upgrade pip
python3.9 -m pip install --no-cache-dir -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput --clear
#gunicorn --config gunicorn-cfg.py core.wsgi
echo "BUILD END"
