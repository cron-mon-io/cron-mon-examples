install:
	python3 -m venv venv && \
		. venv/bin/activate && \
		pip install --upgrade pip && \
		pip install -r requirements.txt

setup-env:
	echo "CRON_MON_SERVER_URL=$(server-url)" > .env && \
		echo "CRON_MON_API_KEY=$(api-key)" >> .env && \
		echo "MONITOR_ID=$(monitor-id)" >> .env

run:
	. venv/bin/activate && \
		set -a && . .env && set +a && \
		python cron-job.py $(duration) --error="$(error)"

remove-venv:
	rm -rf venv
