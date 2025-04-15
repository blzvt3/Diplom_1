import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import Data

@pytest.fixture
def burger_with_3_ingredients():
    burger = Burger()
    ing1 = Ingredient(*Data.ingredient_1)
    ing2 = Ingredient(*Data.ingredient_2)
    ing3 = Ingredient(*Data.ingredient_3)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)
    return burger, ing1, ing2, ing3
