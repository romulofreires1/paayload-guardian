# Use a imagem base do Python 3.9
FROM python:3.9-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o PYTHONPATH para incluir o diretório src
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Copiar os arquivos de dependência para o container
COPY Pipfile Pipfile.lock ./

# Instalar Pipenv e configurar para usar o Python correto
RUN pip install pipenv && pipenv --python $(which python3) install --deploy --ignore-pipfile

# Copiar o restante do código da aplicação
COPY . .

# Definir o ponto de entrada do container
CMD ["pipenv", "run", "python", "main.py"]
