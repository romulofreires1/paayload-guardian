class MonitoringService:
    def __init__(self, metrics, notifier, config_loader, repository, validator):
        """
        Inicializa o serviço de monitoramento com dependências injetadas.

        Args:
            metrics: Um objeto para lidar com métricas (ex: PrometheusMetrics).
            notifier: Um objeto para enviar notificações (ex: EmailNotifier).
            config_loader: Um objeto para carregar a configuração (ex: ConfigLoader).
            repository: Um objeto para buscar os dados (ex: MonitoringRepository).
            validator: Um objeto para validar o payload (ex: PayloadValidation).
        """
        self.metrics = metrics
        self.notifier = notifier
        self.config = config_loader.load_config("config.json")
        self.repository = repository
        self.validator = validator

    def monitor_routes(self):
        for route_config in self.config["routes"]:
            route = route_config["route"]
            expected_payload = route_config["expected_payload"]
            actual_payload = self.repository.fetch_actual_payload(route)

            if actual_payload is None:
                print(f"Failed to fetch payload from {route}")
                continue

            if not self.validator.validate_identical(expected_payload, actual_payload):
                # self.metrics.increment_failure_metric(route)
                self.notifier.notify(
                    route_config["team"], f"Payload mismatch detected for {route}"
                )
            else:
                print(f"Payloads for {route} match successfully.")
