from utils.service import ApiClient
import random

class Specie:
    def __init__(self, base_url):
        self.client = ApiClient(base_url)

    def consulta_species(self):
        caminho = f"species/"
        data = ApiClient.get(self,caminho)
        return data

    def consulta_specie(self):
        caminho = f"species/{random.randint(1,50)}"
        data = ApiClient.get(self,caminho)
        return data

    def consulta_species_invalido(self):
        caminho = f"planets/{random.randint(100,200)}"
        data = ApiClient.get(self,caminho)
        return data
