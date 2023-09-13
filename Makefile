run_dbt:
	docker compose -f dbt_demo/docker-compose.yml up --build

stop_dbt:
	docker compose -f dbt_demo/docker-compose.yml rm -f --volumes