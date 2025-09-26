from features.page.planets_page import Planeta
from behave import then, when
import hamcrest as hc


@when(u'eu consulto o endpoint "/planets/"')
def step_impl(context):
    context.response = Planeta.consulta_planetas(context)


@when(u'eu consulto o endpoint "/planets/1/"')
def step_impl(context):
    context.response = Planeta.consulta_planeta(context)


@when(u'eu consulto o endpoint "/planets/9999/"')
def step_impl(context):
    context.response = Planeta.consulta_planeta_invalido(context)


@then(u'cada planeta deve ter os atributos obrigatórios')
def step_impl(context):
    payload = context.response.json()

    # results existe e é lista não-vazia
    hc.assert_that(payload, hc.has_key("results"))
    planets = payload["results"]
    hc.assert_that(planets, hc.instance_of(list))
    hc.assert_that(planets, hc.has_length(hc.greater_than(0)))

    required = {
        "name", "rotation_period", "orbital_period", "diameter",
        "climate", "gravity", "terrain", "surface_water",
        "population", "residents", "films",
        "created", "edited", "url"
    }

    for p in planets:
        # 1) todos os campos obrigatórios existem
        for k in required:
            hc.assert_that(p, hc.has_key(k), f"Planeta sem campo obrigatório: {k}")

        # 2) tipos/formatos principais
        for k in ["name", "climate", "gravity", "terrain"]:
            hc.assert_that(p[k], hc.instance_of(str), f"Campo {k} não é string")


@then(u'O planeta deve ter os atributos obrigatórios')
def step_impl(context):
    payload = context.response.json()
    hc.assert_that(
        payload,
        hc.all_of(
            hc.has_key("name"),
            hc.has_key("rotation_period"),
            hc.has_key("orbital_period"),
        )
    )
