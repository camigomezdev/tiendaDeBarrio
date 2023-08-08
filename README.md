# Ejercicio práctico de Django

## Instalación:

```
python -m venv venv

# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Para crear un super usuario y acceder al admin:

```
python manage.py createsuperuser
```

docs: https://docs.djangoproject.com/en/4.1/ref/settings/#databases
