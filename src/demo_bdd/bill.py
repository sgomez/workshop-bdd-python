from math import floor
from typing import List
import unittest

from demo_bdd.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()


class Bill:
    VAT = 1.10
    menus: List[Menu]
    cash: int
    used_points: int
    total_before_vat: int

    def __init__(self) -> None:
        self.menus = []
        self.cash = 0
        self.used_points = 0
        self.total_before_vat = 0

    def add(self, menu: Menu) -> None:
        self.menus.append(menu)
        self.total_before_vat += menu.price

    @property
    def total(self) -> int:
        return int(self.total_before_vat * self.VAT)

    def pay_with_cash(self, total: int) -> None:
        self.cash = total

    def rest_to_pay(self) -> int:
        return self.total - self.cash - floor(self.used_points / 10) * 100

    def points(self) -> int:
        if self.used_points > 0:
            return 0

        return floor(self.total_before_vat / 100)

    def pay_with_points(self, used_points: int) -> None:
        self.used_points = used_points
