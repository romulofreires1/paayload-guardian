# Define variáveis para o diretório fonte
SRC_DIR=src/
DOCKER_COMPOSE_FILE := docker-compose.yml

# Instalar as dependências do projeto
install:
	@echo "Instalando dependências com pipenv..."
	pipenv install --dev

# Rodar Flake8 para linting
lint:
	@echo "Executando Flake8..."
	pipenv run flake8 $(SRC_DIR)

# Rodar Black para formatação de código
format:
	@echo "Formatando código com Black..."
	pipenv run black $(SRC_DIR)

# Organizar imports com isort
sort-imports:
	@echo "Organizando imports com isort..."
	pipenv run isort $(SRC_DIR)

# Rodar Pylint para análise de código mais rigorosa
pylint:
	@echo "Executando Pylint..."
	pipenv run pylint --rcfile=.pylintrc $(SRC_DIR)

# Executar todas as ferramentas de uma vez (lint, format, sort-imports, pylint)
check:
	@echo "Executando linting, formatação e organização de imports..."
	make lint
	make format
	make sort-imports
	make pylint

# Configurar pre-commit hooks
pre-commit-install:
	@echo "Instalando hooks do pre-commit..."
	pipenv run pre-commit install

# Rodar pre-commit manualmente
pre-commit-run:
	@echo "Executando pre-commit hooks..."
	pipenv run pre-commit run --all-files

# Rodar
run:
	@echo "Executando a aplicação PayloadGuardian..."
	PYTHONPATH=src pipenv run python main.py

# Testes
test:
	@echo "Executando testes..."
	pipenv run python -m unittest discover -s tests

# Alvo para buildar as imagens Docker
docker-build:
	@echo "Building Docker images..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) build

# Alvo para subir os containers Docker
docker-up:
	@echo "Starting Docker containers..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) up

# Alvo para parar os containers Docker
docker-stop:
	@echo "Stopping Docker containers..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) stop

# Alvo para remover os containers Docker
docker-down:
	@echo "Removing Docker containers..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

# Alvo para rodar os testes dentro do container do payload-guardian
docker-test:
	@echo "Running tests inside Docker..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) run payload-guardian pipenv run python -m unittest discover -s tests

# Alvo para visualizar os logs dos containers
docker-logs:
	@echo "Displaying Docker logs..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) logs -f

# Alvo para rebuildar os containers Docker (sem cache)
docker-rebuild:
	@echo "Rebuilding Docker images (without cache)..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) build --no-cache

# Alvo para acessar o shell dentro do container payload-guardian
docker-shell:
	@echo "Accessing shell of payload-guardian container..."
	docker exec -it payload_guardian /bin/sh

