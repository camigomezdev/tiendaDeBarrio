run:
	python manage.py runserver --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

createsuperuser:
	python manage.py createsuperuser --settings=settings.local

run-prod:
	python manage.py runserver --settings=settings.prod