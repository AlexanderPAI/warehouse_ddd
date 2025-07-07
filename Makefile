.PHONY: build up test

build:
	docker-compose build

up:
	docker-compose up

test:
	docker-compose up --build -d
	docker exec warehouse_backend pytest -v tests/
