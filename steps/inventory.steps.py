from behave import *

@when("inventory: I click on the settings button")
def step_impl(context):
    context.inventory_page.click.click_settings_btn()
@then ('inventory: I am in an inventory page')
def step_impl(context):
    context.inventory_page.goto_inventory_pageURL()

@then ('inventory: Settings list is displayed')
def step_impl(context):
    context.inventory_page.check_settings_list()
