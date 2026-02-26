import requests
from src.config.settings import BASE_URL

class ApiClient:
    def __init__(self, base_url: str = BASE_URL, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.get(url, timeout=self.timeout, **kwargs)

    def post(self, path: str, data=None, json=None, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.post(url, data=data, json=json, timeout=self.timeout, **kwargs)