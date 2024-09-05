from src.infrastructure.fetcher.http_fetcher import HttpFetcher
from src.application.services.monitoring_service import MonitoringService
from src.config.config_loader import ConfigLoader
from src.domain.models.validation import PayloadValidation
from src.infrastructure.metrics.prometheus_metrics import PrometheusMetrics
from src.infrastructure.notifiers.email_notifier import EmailNotifier

if __name__ == "__main__":
    metrics = PrometheusMetrics()
    notifier = EmailNotifier()
    config_loader = ConfigLoader()
    validator = PayloadValidation()
    fetcher = HttpFetcher()

    service = MonitoringService(metrics, notifier, config_loader, validator, fetcher)
    service.monitor_routes_continuously()
