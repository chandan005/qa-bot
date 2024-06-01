.PHONY: install format lint run docker-build docker-run clean

install: pipenv install --dev

format:
	pipenv run black .
	pipenv run isort .

lint:
	pipenv run black --check .
	pipenv run isort --check-only .

# Dev
run-dev:
	ENV=dev pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Prod
run-prod:
	ENV=prod pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

docker-build:
	docker build -t question_answering_bot .

docker-run-dev:
	docker run -d --name question_answering_bot_container -p 8000:8000 -e ENV=dev question_answering_bot

docker-run-prod:
	docker run -d --name question_answering_bot_container -p 8000:8000 -e ENV=prod question_answering_bot

clean:
	docker rm -f question_answering_bot_container || true
	docker rmi -f question_answering_bot || true
