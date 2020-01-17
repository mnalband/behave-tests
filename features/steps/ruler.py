@given("I want to check ruler state")
def step_impl(context):
    """Stub for feature verbosity, actual steps are performed in then."""
    return True

@then("I see range '{ruler_range}'")
def step_impl(context, ruler_range):
    assert context.main_page.get_ruler_value() == ruler_range

@then("Ruler controls")
def step_impl(context):
    assert context.main_page.get_ruler_more().is_displayed()
    assert context.main_page.get_ruler_less().is_displayed()

@then("Ruler start")
def step_impl(context):
    assert context.main_page.get_ruler_start().is_displayed()

@then("Ruler continue '{times}' times")
def step_impl(context, times):
    assert len(context.main_page.get_ruler_continue()) == int(times)

@then("Input numbers are in range '{ruler_range}'")
def step_impl(context, ruler_range):
    assert int(context.main_page.get_first_number()) <= int(ruler_range)
    assert int(context.main_page.get_second_number()) <= int(ruler_range)

@given("I want to increase ruler range {times} times")
def step_impl(context, times):
    for _ in range(int(times)):
        context.main_page.get_ruler_more().click()

@given("I want to decrease ruler range {times} times")
def step_impl(context, times):
    for _ in range(int(times)):
        context.main_page.get_ruler_less().click()
