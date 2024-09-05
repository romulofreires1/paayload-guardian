# (Em construção) PayloadGuardian

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
- **Arquitetura Hexagonal** e **Clean Code**: Aplicação de boas práticas para garantir um código limpo, de fácil manutenção e extensível.

## Estrutura do Projeto

```plaintext
monitoring_service/
│
├── src/
│   ├── application/
│   │   ├── services/
│   │   │   └── monitoring_service.py
│   │   ├── repositories/
│   │   │   └── monitoring_repository.py
│   │   ├── dtos/
│   │   │   └── notification_dto.py
│   │   └── interfaces/
│   │       └── notifier.py
│   ├── domain/
│   │   ├── models/
│   │   │   └── validation.py
│   ├── infrastructure/
│   │   ├── notifiers/
│   │   │   └── email_notifier.py
│   │   └── metrics/
│   │       └── prometheus_metrics.py
│   └── config/
│       └── config_loader.py
│
└── config.json
