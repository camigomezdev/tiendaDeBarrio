run:
	python manage.py runserver --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

createsuperuser:
	python manage.py createsuperuser --settings=settings.local

run-prod:
	python manage.py runserver --settings=settings.prod

# call with make copy-db -e DB_FILE=<your-file-name>
copy-db:
	mysqldump -u root tienda_de_barrio_db > $(DB_FILE)

clear-local-db:
	echo "DROP DATABASE IF EXISTS tienda_de_barrio_db; CREATE DATABASE tienda_de_barrio_db;" | mysql -u root

# call with make import-db -e DB_FILE=<your-file-name>
import-db: clear-local-db
	mysql -u root tienda_de_barrio_db < $(DB_FILE)