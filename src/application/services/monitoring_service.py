class MonitoringService:
    def __init__(self, metrics, notifier, config_loader, repository, validator):
        self.metrics = metrics
        self.notifier = notifier
        self.config = config_loader.load_config("config.json")
        self.repository = repository
        self.validator = validator

    def monitor_routes(self):
        routes = self.config["routes"]
        for route_config in routes:
            self.monitor_single_route(route_config)

    def monitor_single_route(self, route_config):
        route = route_config["route"]
        expected_payload = route_config["expected_payload"]
        actual_payload = self.fetch_payload(route)

        if actual_payload is None:
            self.handle_payload_fetch_failure(route)
            return

        if not self.validator.validate_identical(expected_payload, actual_payload):
            self.handle_payload_mismatch(route, route_config["team"])
        else:
            self.handle_payload_success(route)

    def fetch_payload(self, route):
        return self.repository.fetch_actual_payload(route)

    def handle_payload_fetch_failure(self, route):
        print(f"Failed to fetch payload from {route}")

    def handle_payload_mismatch(self, route, team):
        self.notifier.notify(team, f"Payload mismatch detected for {route}")
        # self.metrics.increment_failure_metric(route)

    def handle_payload_success(self, route):
        print(f"Payloads for {route} match successfully.")
