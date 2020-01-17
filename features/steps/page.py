import os
from time import sleep


@when("I want to open main page")
@given("I want to open main page")
def step_impl(context):
    path = os.path.abspath("./index.html")
    context.browser.get(f"file://{path}")

@then("I see the default title")
def step_impl(context):
    assert context.main_page.get_title() == "Addition and subtraction to 20"

@then("All elements: calculator and ruler")
def step_impl(context):
    assert context.main_page.get_first_number_element().is_displayed()
    assert context.main_page.get_operator_element().is_displayed()
    assert context.main_page.get_second_number_element().is_displayed()
    assert context.main_page.get_result_element().is_displayed()
    assert context.main_page.get_submit_element().is_displayed()
    assert context.main_page.get_ruler_element().is_displayed()

@then("Not operation result")
def step_impl(context):
    assert not context.main_page.get_operation_result_element().is_displayed()

@then("First input is pre-filled with int")
def step_impl(context):
    assert int(context.main_page.get_first_number())

@then("Second input is pre-filled with int")
def step_impl(context):
    assert int(context.main_page.get_second_number())

@then("Operator is either + or -")
def step_impl(context):
    assert context.main_page.get_operator() in ["+", "-"]

@then("Result input is empty")
def step_impl(context):
    assert context.main_page.get_result() == ""
