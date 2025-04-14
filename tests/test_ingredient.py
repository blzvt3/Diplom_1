import pytest
from praktikum.ingredient import Ingredient
from data import Data

class TestIngredient:
    @pytest.mark.parametrize(("ingredient_type", "name", "price"), Data.ingredient_data)
    def test_get_price_of_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(("ingredient_type", "name", "price"), Data.ingredient_data)
    def test_get_name_of_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(("ingredient_type", "name", "price"), Data.ingredient_data)
    def test_get_type_of_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
