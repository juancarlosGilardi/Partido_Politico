from typing import Optional
import requests
import logging

APIS_TOKEN = "apis-token-9763.PDu5uWAdY1pfKzTEHZUb3gM9gNYAmP9r"

class ApisNetPe:

    BASE_URL = "https://api.apis.net.pe"

    def __init__(self, token: str = None) -> None:
        self.token = APIS_TOKEN

    def _get(self, endpoint: str, params: dict) -> Optional[dict]:
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        try:
            response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error during request to {endpoint}: {e}")
            return None

    def get_person(self, dni: str) -> Optional[dict]:
        return self._get("/v2/reniec/dni", {"numero": dni})

# Crear una instancia de ApisNetPe
api_client = ApisNetPe()

# Llamar al método get_person con el DNI
result = api_client.get_person("08196299")
print(result)