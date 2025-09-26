from features.data.planets_json import planets_get
from utils.service import ApiClient
import random

class Planeta:
    def __init__(self, base_url):
        self.client = ApiClient(base_url)

    def consulta_planetas(self):
        caminho = f"planets/"
        data = ApiClient.get(self,caminho)
        return data

    def consulta_planeta(self):
        caminho = f"planets/{random.randint(1,50)}"
        data = ApiClient.get(self,caminho)
        return data

    def consulta_planeta_invalido(self):
        caminho = f"planets/{random.randint(100,200)}"
        data = ApiClient.get(self,caminho)
        return data
