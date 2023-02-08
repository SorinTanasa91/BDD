from behave import *


@when("inventory: I click on the settings button")
def step_impl(context):
    context.inventory_page.click.click_settings_btn()


@then('inventory: I am in an inventory page')
def step_impl(context):
    context.inventory_page.goto_inventory_pageURL()


@then('inventory: Settings list is displayed')
def step_impl(context):
    context.inventory_page.check_settings_list()

@then('Then inventory: Logo is displayed')
def step_impl(context):
    context.inventory_page.check_logo_icon()
@When ('inventory: I click on the cart')
def step_impl(context):
    context.inventory_page.click_shopping_cart()
@Then ('cart: Url has changed')
def step_impl(context):
    context.shoppingCartPage.getShoppingCartURL()
