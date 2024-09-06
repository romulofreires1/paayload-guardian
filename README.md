
# PayloadGuardian

## Descrição

**PayloadGuardian** é um serviço Python projetado para monitorar periodicamente os payloads de diferentes rotas configuradas. O objetivo é garantir que os payloads recebidos de outras APIs ou serviços sejam idênticos aos esperados. Em caso de discrepâncias, o serviço registra uma métrica de falha no Prometheus e envia uma notificação por email ao time responsável. O design do sistema é extensível, permitindo adicionar novas validações e tipos de notificações facilmente no futuro.

## Funcionalidades

- **Monitoramento de Payloads**: Verifica periodicamente os payloads das rotas configuradas para assegurar a conformidade.
- **Validação de Dados**: Compara o payload recebido com o esperado para identificar discrepâncias.
- **Registro de Métricas**: Utiliza o Prometheus para registrar falhas de validação de payloads.
- **Notificações**: Envia notificações por email para o time responsável quando uma discrepância é detectada.
- **Extensibilidade**: Projetado para facilitar a adição de novas validações e tipos de notificações.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do serviço.
- **Requests**: Biblioteca utilizada para realizar requisições HTTP.
- **Prometheus-client**: Biblioteca para integração com Prometheus para registro de métricas.
- **Pipenv**: Usado para gerenciar dependências e ambiente virtual.
- **Arquitetura Hexagonal** e **Clean Code**: Aplicação de boas práticas para garantir um código limpo, de fácil manutenção e extensível.
- **Docker** e **Docker Compose**: Para rodar o ambiente de forma isolada e reprodutível, incluindo serviços mock.
- **WireMock**: Ferramenta utilizada para mockar APIs.

## Comandos

### Instalação das dependências

Para instalar as dependências do projeto, utilize o seguinte comando:

```bash
pipenv install --dev
```

### Executar o serviço com Docker

Para rodar o serviço **PayloadGuardian** com Docker, execute o seguinte comando:

```bash
make docker-up
```

Isso irá iniciar o serviço **PayloadGuardian** junto com o serviço **WireMock** que mocka as APIs. Para garantir que as imagens Docker estão atualizadas, use:

```bash
make docker-build
```

### Subir apenas o mock-api

Caso precise apenas do **mock-api** (WireMock), você pode usar o seguinte comando:

```bash
docker-compose up mock-api -d
```

### Parar e remover containers

Para parar e remover os containers:

```bash
make docker-down
```

### Verificar a qualidade do código

O projeto utiliza ferramentas como **Flake8** e **Pylint** para garantir a qualidade do código. Para executar as verificações de qualidade, utilize os seguintes comandos:

#### Testing

```bash
make test
```

#### Linting (Flake8 e Pylint)

```bash
make lint
make pylint
```

#### Formatação de código (Black e isort)

```bash
make format
make sort-imports
```

### Configurar o pre-commit

O projeto usa hooks do **pre-commit** para automatizar verificações de qualidade antes dos commits. Para configurar o pre-commit, execute:

```bash
make pre-commit-install
```

### Executar pre-commit manualmente

Para rodar o pre-commit manualmente em todos os arquivos:

```bash
make pre-commit-run
```

## Configuração

As configurações para monitoramento de rotas, equipes responsáveis e tipos de validação são definidas em um arquivo JSON (`config.json`). Este arquivo deve ser configurado conforme necessário para atender às necessidades específicas do seu ambiente.

### Alterações no arquivo de configuração para rodar com Docker

Quando for rodar o serviço no Docker, os endpoints nas rotas do `config.json` devem ser alterados para o nome do serviço **mock-api**. Exemplo:

```json
{
    "routes": [
        {
            "route": "http://mock-api:5000/test",
            "team": "team@example.com",
            "validation": "identical",
            "expected_payload": {
                "key1": "value1",
                "key2": "value2"
            },
            "check_interval": 60
        }
    ]
}
```

### Adicionar Endpoints de Testes no WireMock

O serviço **WireMock** mocka as APIs utilizadas no **PayloadGuardian**. Para adicionar novos endpoints de teste, você pode criar arquivos JSON de mapeamento na pasta `wiremock/mappings/`.

Exemplo de arquivo `wiremock/mappings/test-mock.json` para mockar o endpoint `/test`:

```json
{
  "request": {
    "method": "GET",
    "url": "/test"
  },
  "response": {
    "status": 200,
    "jsonBody": {
      "key1": "value1",
      "key2": "value2"
    },
    "headers": {
      "Content-Type": "application/json"
    }
  }
}
```

Após adicionar ou alterar endpoints no WireMock, você pode reiniciar o serviço mock com:

```bash
make docker-down
make docker-up
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias, novas funcionalidades ou correções de bugs. Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas alterações (`git commit -m 'Adicionar nova feature'`).
4. Faça o push para a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.