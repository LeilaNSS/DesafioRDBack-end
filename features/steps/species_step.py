from features.page.species_page import Specie
from behave import then, when
import hamcrest as hc


@when(u'eu consulto o endpoint "/species/"')
def step_impl(context):
    context.response = Specie.consulta_specie(context)


@when(u'eu consulto o endpoint "/species/1/"')
def step_impl(context):
    context.response = Specie.consulta_species(context)


@when(u'eu consulto o endpoint "/species/9999/"')
def step_impl(context):
    context.response = Specie.consulta_species_invalido(context)

@then(u'cada specie deve ter os atributos obrigatórios')
def step_impl(context):
    def step_validate_species_required_fields(context):
        payload = context.response.json()

        # Estrutura básica do payload de lista
        hc.assert_that(payload, hc.all_of(
            hc.has_key("count"),
            hc.has_key("next"),
            hc.has_key("previous"),
            hc.has_key("results"),
        ))

        results = payload["results"]
        hc.assert_that(results, hc.instance_of(list))
        hc.assert_that(results, hc.has_length(hc.greater_than(0)))

        # Campos obrigatórios por espécie
        required = {
            "name", "classification", "designation", "average_height",
            "skin_colors", "hair_colors", "eye_colors", "average_lifespan",
            "homeworld", "language", "people", "films",
            "created", "edited", "url"
        }

        # 1) Cada item tem todas as chaves obrigatórias
        hc.assert_that(
            results,
            hc.every_item(
                hc.all_of(*(hc.has_key(k) for k in required))
            )
        )

        # 2) (Opcional, mas útil) As coleções existem como listas
        hc.assert_that(
            results,
            hc.every_item(
                hc.has_entries(
                    people=hc.instance_of(list),
                    films=hc.instance_of(list),
                )
            )
        )

@then(u'A specie deve ter os atributos obrigatórios')
def step_impl(context):
    payload = context.response.json()
    hc.assert_that(payload, hc.has_key("results"))
    results = payload["results"]

    hc.assert_that(results, hc.instance_of(list))
    hc.assert_that(results, hc.has_length(hc.greater_than(0)))
