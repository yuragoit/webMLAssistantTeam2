echo "BUILD START"
python -m pip install --upgrade pip
python -m pip install --no-cache-dir -r requirements.txt
python -m pip install pysqlite
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput --clear
#gunicorn --config gunicorn-cfg.py core.wsgi
echo "BUILD END"
