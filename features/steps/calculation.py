@given("I want to calculate given numbers")
def step_impl(context):
    first_number = int(context.main_page.get_first_number())
    second_number = int(context.main_page.get_second_number())
    operator = context.main_page.get_operator()
    result = None
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    # Ensure that operator was either + or - and result was calculated
    assert result
    context.result = result


@then("Input correct answer")
def step_impl(context):
    result = context.main_page.get_result_element()
    result.send_keys(context.result)


@then("Input incorrect answer")
def step_impl(context):
    result = context.main_page.get_result_element()
    result.send_keys("text")


@then("Click submit")
def step_impl(context):
    context.main_page.get_submit_element().click()


@then("See happy elephant")
def step_impl(context):
    assert context.main_page.get_good_result().is_displayed()


@then("See angry monkey")
def step_impl(context):
    assert context.main_page.get_bad_result().is_displayed()
