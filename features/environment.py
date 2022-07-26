from behave.runner import Context

from demo_bdd.bill import Bill


def before_scenario(context: Context, scenario):
    context.menus = {}
    context.bill = Bill()
