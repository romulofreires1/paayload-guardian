
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

## Comandos

### Instalação das dependências

Para instalar as dependências do projeto, utilize o seguinte comando:

```bash
pipenv install --dev
```

### Executar o serviço

Para rodar o serviço **PayloadGuardian**, execute o comando abaixo:

```bash
make run
```

Isso executará o monitoramento contínuo de payloads conforme definido no arquivo de configuração.

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

Exemplo de `config.json`:

```json
{
    "routes": [
        {
            "route": "http://example.com/api/data",
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

## Contribuição

Sinta-se à vontade para contribuir com melhorias, novas funcionalidades ou correções de bugs. Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas alterações (`git commit -m 'Adicionar nova feature'`).
4. Faça o push para a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.