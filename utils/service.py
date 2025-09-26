import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    @staticmethod
    def header_generico():
        return {
            "Content-Type": "application/json"
        }

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        header = ApiClient.header_generico()
        response = requests.get(url, params=params, headers=header)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, headers=headers)
        return response
