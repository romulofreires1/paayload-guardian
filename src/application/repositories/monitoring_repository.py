import requests


class MonitoringRepository:
    def fetch_actual_payload(self, route):
        response = requests.get(route, timeout=0.5)
        if response.status_code == 200:
            return response.json()
        return None
