import pytest
from praktikum.bun import Bun
from data import Data

class TestBun:
    @pytest.mark.parametrize(("name", "price"), Data.bun_data)
    def test_get_name_of_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(("name", "price"), Data.bun_data)
    def test_get_price_of_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
