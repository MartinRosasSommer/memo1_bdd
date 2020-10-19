from behave import *


@given("{amount} pesos")
def step_impl(context, amount):
    context.amount = int(amount)


@when("trying to pay")
def step_impl(context):
    assert(context.amount > 10)
    if context.amount > 10:
        context.money_received = True


@then("the cashier should receive the money")
def step_impl(context):
    assert context.failed is False
    assert context.money_received is True


@given('A car')
def step_impl(context):
    context.speed = 0


@when('Stepping on accelerator pedal')
def step_impl(context):
    context.speed += 10


@then('Speed should raise')
def step_impl(context):
    assert context.failed is False
    assert context.speed > 0


@when('Stepping on brake pedal')
def step_impl(context):
    context.speed = 0


@then('Speed should decrease')
def step_impl(context):
    assert context.failed is False
    assert context.speed == 0
