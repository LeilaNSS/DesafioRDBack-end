from hamcrest import assert_that, is_,equal_to


@then(u'o status code deve ser 200')
def step_impl(context):
    assert_that(context.response.status_code,equal_to(200))

@then(u'o status code deve ser 404')
def step_impl(context):
    assert_that(context.response.status_code,equal_to(404))