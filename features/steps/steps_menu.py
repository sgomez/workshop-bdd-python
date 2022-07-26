from behave import given, then, when

from demo_bdd.bill import Bill
from demo_bdd.menu import Menu


@given("the following menus")
def step_impl(context):

    for row in context.table:
        number = int(row["number"])
        price = int(row["price"]) * 100
        menu = Menu(number=number, price=price)
        context.menus[number] = menu


@given("that I have bought {qty} menu of number {number}")
@given("that I have bought {qty} menus of number {number}")
def step_impl(context, qty: int, number: int):
    qty = int(qty)
    number = int(number)
    menu = context.menus[number]

    [context.bill.add(menu=menu) for x in range(qty)]


@when("I ask for the bill, I receive a bill for {total} euros")
def step_impl(context, total):
    total = int(total) * 100

    assert context.bill.total == total


@when("I pay in cash with {total} euros")
def step_impl(context, total):
    total = int(total) * 100

    context.bill.pay_with_cash(total)


@then("the bill is paid")
def step_impl(context):
    rest_to_pay = context.bill.rest_to_pay()

    assert rest_to_pay == 0


@then("I have earned {earned_points} points")
def step_impl(context, earned_points):
    earned_points = int(earned_points)

    points = context.bill.points()

    assert points == earned_points


@when("I pay with {points} points and {euros} euros")
def step_impl(context, points, euros):
    points = int(points)
    cents = int(euros) * 100

    context.bill.pay_with_cash(cents)
    context.bill.pay_with_points(points)
