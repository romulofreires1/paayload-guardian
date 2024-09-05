from application.repositories.monitoring_repository import MonitoringRepository
from application.services.monitoring_service import MonitoringService
from config.config_loader import ConfigLoader
from domain.models.validation import PayloadValidation
from infrastructure.metrics.prometheus_metrics import PrometheusMetrics
from infrastructure.notifiers.email_notifier import EmailNotifier


metrics = PrometheusMetrics()
notifier = EmailNotifier()
config_loader = ConfigLoader()
repository = MonitoringRepository()
validator = PayloadValidation()

service = MonitoringService(metrics, notifier, config_loader, repository, validator)
service.monitor_routes_continuously()