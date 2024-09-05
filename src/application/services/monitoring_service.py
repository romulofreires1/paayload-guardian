from application.repositories.monitoring_repository import MonitoringRepository
from config.config_loader import ConfigLoader
from domain.models.validation import PayloadValidation
from infrastructure.metrics.prometheus_metrics import PrometheusMetrics
from infrastructure.notifiers.email_notifier import EmailNotifier


class MonitoringService:
    def __init__(self):
        self.metrics = PrometheusMetrics()
        self.notifier = EmailNotifier()
        self.config = ConfigLoader.load_config("config.json")
        self.repository = MonitoringRepository()

    def monitor_routes(self):
        for route_config in self.config["routes"]:
            route = route_config["route"]
            expected_payload = route_config["expected_payload"]
            actual_payload = self.repository.fetch_actual_payload(route)

            if actual_payload is None:
                print(f"Failed to fetch payload from {route}")
                continue

            if not PayloadValidation.validate_identical(
                expected_payload, actual_payload
            ):
                # self.metrics.increment_failure_metric(route)
                self.notifier.notify(
                    route_config["team"], f"Payload mismatch detected for {route}"
                )
            else:
                print(f"Payloads for {route} match successfully.")


if __name__ == "__main__":
    service = MonitoringService()
    service.monitor_routes()
