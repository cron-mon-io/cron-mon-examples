run:
	docker-compose up api app monitor

purge-volumes:
	docker compose down app db && docker volume rm cron-mon-postgres-data cron-mon-caddy-data
