build:
	docker compose -f local.yaml up --build -d --remove-orphans

up:
	docker compose -f local.yaml up -d

down:
	docker compose -f local.yaml down

down-v:
	docker compose -f local.yaml down -v

show-logs:
	docker compose -f local.yaml logs

show-logs-api:
	docker compose -f local.yaml logs api

makemigrations:
	docker compose -f local.yaml run --api python manage.py makemigrations

migrate:
	docker compose -f local.yaml run --rm api python manage.py migrate

collectstatic:
	docker compose -f local.yaml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yaml run --rm api python manage.py createsuperuser

db-volume:
	docker volume inspect api_estate_prod_postgres_data

mailpit-volume:
	docker volume inspect api_estate_prod_mailpit_data

estate-db:
	docker compose -f local.yaml exec postgres psql --username=fiston --dbname=estate