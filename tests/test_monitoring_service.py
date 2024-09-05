import unittest
from unittest.mock import MagicMock
from src.application.services.monitoring_service import MonitoringService

class TestMonitoringService(unittest.TestCase):

    def setUp(self):
        self.metrics = MagicMock()
        self.notifier = MagicMock()
        self.config_loader = MagicMock()
        self.validator = MagicMock()
        self.fetcher = MagicMock()

        self.config_loader.load_config.return_value = {
            "routes": [
                {
                    "route": "http://example.com/api/data",
                    "expected_payload": {"key": "value"},
                    "team": "team@example.com",
                    "check_interval": 60
                }
            ]
        }

        self.service = MonitoringService(
            metrics=self.metrics,
            notifier=self.notifier,
            config_loader=self.config_loader,
            validator=self.validator,
            fetcher=self.fetcher
        )

    def test_monitor_single_route_success(self):
        self.fetcher.fetch.return_value = {"key": "value"}
        self.validator.validate_identical.return_value = True
        self.service.monitor_single_route(self.config_loader.load_config()["routes"][0])
        self.notifier.notify.assert_not_called()
        self.metrics.increment_failure_metric.assert_not_called()

    def test_monitor_single_route_mismatch(self):
        self.fetcher.fetch.return_value = {"key": "wrong_value"}
        self.validator.validate_identical.return_value = False
        self.service.monitor_single_route(self.config_loader.load_config()["routes"][0])
        self.notifier.notify.assert_called_once_with(
            "team@example.com", "Payload mismatch detected for http://example.com/api/data"
        )

    def test_monitor_single_route_fetch_failure(self):
        self.fetcher.fetch.return_value = None
        self.service.monitor_single_route(self.config_loader.load_config()["routes"][0])
        self.notifier.notify.assert_not_called()
        self.metrics.increment_failure_metric.assert_not_called()

if __name__ == "__main__":
    unittest.main()
