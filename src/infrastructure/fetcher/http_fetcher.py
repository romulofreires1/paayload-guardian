import requests


class HttpFetcher:
    def fetch(self, route):
        try:
            response = requests.get(route, timeout=0.5)
            if response.status_code == 200:
                return response.json()
            print(f"Failed to fetch payload from {route}")
            return None
        except requests.RequestException as e:
            print(f"Error fetching payload from {route}: {e}")
            return None
