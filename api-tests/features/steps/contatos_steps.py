import requests
from behave import when, then

BASE_URL = "https://apidetarefas.docs.apiary.io"

@when('eu faço uma requisição GET para "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.get(BASE_URL + endpoint)

@then('o status code deve ser {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, \
        f"Esperado {status_code}, mas foi {context.response.status_code}"