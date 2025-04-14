from praktikum.database import Database
from data import Data

class TestData:
    def test_available_buns(self):
        db = Database()
        buns_data = [(bun.get_name(), bun.get_price()) for bun in db.available_buns()]
        assert buns_data == Data.database_buns_data

    def test_available_ingredients(self):
        db = Database()
        ingredients_data = [(ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for ingredient in db.available_ingredients()]
        assert ingredients_data == Data.database_ingredients_data