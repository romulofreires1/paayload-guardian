from prometheus_client import Counter


class PrometheusMetrics:
    def __init__(self):
        self.failure_counter = Counter(
            "payload_validation_failures", "Number of payload validation failures"
        )

    def increment_failure_metric(self, route):
        self.failure_counter.labels(route=route).inc()
