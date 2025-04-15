import pytest
from unittest.mock import Mock
from data import Data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

class TestBurger:
    @pytest.mark.parametrize(("name", "price"), Data.bun_data)
    def test_set_bun(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)

        assert burger.bun.get_name() == name
        assert burger.bun.get_price() == price

    def test_add_one_ingredient_with_mocks(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_type.return_value = "SAUCE"
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == "hot sauce"
        assert burger.ingredients[0].get_price() == 100
        assert burger.ingredients[0].get_type() == "SAUCE"

    def test_add_three_ingredients(self, burger_with_3_ingredients):
        burger, ing1, ing2, ing3 = burger_with_3_ingredients

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] is ing1
        assert burger.ingredients[1] is ing2
        assert burger.ingredients[2] is ing3

    def test_remove_one_ingredient(self):
        burger = Burger()
        ing = Ingredient(*Data.ingredient_1)
        burger.add_ingredient(ing)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_remove_middle_ingredient(self, burger_with_3_ingredients):
        burger, ing1, ing2, ing3 = burger_with_3_ingredients
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] is ing1
        assert burger.ingredients[1] is ing3

    def test_move_ingredient_forward(self, burger_with_3_ingredients):
        burger, ing1, ing2, ing3 = burger_with_3_ingredients
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    def test_move_ingredient_backward(self, burger_with_3_ingredients):
        burger, ing1, ing2, ing3 = burger_with_3_ingredients
        burger.move_ingredient(2, 0)

        assert burger.ingredients == [ing3, ing1, ing2]

    def test_get_price_with_mocks(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 200
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 100 * 2 + 200

    @pytest.mark.parametrize(("name", "price"), Data.bun_data)
    def test_get_price_only_bun(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)

        assert burger.get_price() == price * 2