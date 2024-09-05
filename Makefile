# Define variáveis para o diretório fonte
SRC_DIR=src/

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


run:
	@echo "Executando a aplicação PayloadGuardian..."
	PYTHONPATH=src pipenv run python src/__init__.py

