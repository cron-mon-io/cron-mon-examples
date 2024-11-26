install:
	docker compose pull && \
		docker compose run --rm api ./cron-mon create-monitor \
			--name "Example Monitor" \
			--tenant cron-mon \
			--expected 60 \
			--grace 10

run: run-single-tenant

run-single-tenant:
	REALM=cron-mon-single-tenant $(_run)

run-user-tenant:
	REALM=cron-mon-user-tenant $(_run)

purge-volumes:
	docker compose down app db && docker volume rm cron-mon-postgres-data cron-mon-caddy-data

define _run
	docker compose up api app monitor
endef
