import unittest
from exercises.second_part import ex5

class Test__get_outfamily_and_restricted_ingredients(unittest.TestCase):
    def test__example1(self):
        preferences = {1: "not chicken", 2: "not onion", 3: "not beef", 4: "not pepper", 5: "not butter"}
        restrictions = {"allergy sufferers": "5", "vegans": "135", "non-onion lovers": "2"}
        family_kwarg = {'Papa':["non-onion lovers"], 'Mama': []}
        family_out_act, restr_ingred_act = ex5.get_outfamily_and_restricted_ingredients(preferences,
                                                                                    restrictions,
                                                                                    family_kwarg)
        self.assertEqual(family_out_act, ['Papa - onion', 'Mama - no restrictions'])
        self.assertEqual(restr_ingred_act, {'onion'})


    def test__many_restriction_ids(self):
        preferences = {1: "not chicken", 2: "not onion", 3: "not beef", 4: "not pepper", 5: "not butter"}
        restrictions = {"allergy sufferers": "5", "vegans": "135", "non-onion lovers": "2"}
        family_kwarg = {'Papa':["vegans"]}
        family_out_act, restr_ingred_act = ex5.get_outfamily_and_restricted_ingredients(preferences,
                                                                                    restrictions,
                                                                                    family_kwarg)
        self.assertEqual(family_out_act, ['Papa - chicken, beef, butter'])
        self.assertEqual(restr_ingred_act, {'beef', 'chicken', 'butter'})

    def test__two_kwargs(self):
        preferences = {1: "not chicken", 2: "not onion", 3: "not beef", 4: "not pepper", 5: "not butter"}
        restrictions = {"allergy sufferers": "5", "vegans": "135", "non-onion lovers": "2"}
        family_kwarg = {'Papa':["vegans", "non-onion lovers"]}
        family_out_act, restr_ingred_act = ex5.get_outfamily_and_restricted_ingredients(preferences,
                                                                                    restrictions,
                                                                                    family_kwarg)
        self.assertEqual(family_out_act, ['Papa - chicken, beef, butter, onion'])
        self.assertEqual(restr_ingred_act, {'onion', 'chicken', 'beef', 'butter'})


class FilterByTimeTestCase(unittest.TestCase):
    def test_example1(self):
        recipes = {
            "time_variative" : [30, 25, 15, 35],
            "time_strict" : [55, 100, 15, 30]
        }
        max_time = 100
        n_members = 5
        allowed_ind = range(4)
        actual = ex5.filter_recipes_by_time(recipes,
                                            allowed_ind,
                                            max_time,
                                            n_members)
        self.assertEqual([0, 2, 3], actual)

    def test_eq(self):
        recipes = {
            "time_variative": [50],
            "time_strict": [90]
        }
        max_time = 100
        n_members = 5
        allowed_ind = range(len(recipes['time_variative']))
        actual = ex5.filter_recipes_by_time(recipes,
                                            allowed_ind,
                                            max_time,
                                            n_members)
        self.assertEqual([0], actual)

    def test_different(self):
        recipes = {
            "time_variative": [10, 10, 1000],
            "time_strict": [8, 7, 2]
        }
        max_time = 10
        n_members = 5
        allowed_ind = range(len(recipes['time_variative']))
        actual = ex5.filter_recipes_by_time(recipes,
                                            allowed_ind,
                                            max_time,
                                            n_members)
        self.assertEqual([0, 1], actual)


class FilterByIngredientsTestCase(unittest.TestCase):
    def test_example1(self):
        recipes = {"ingredients" : [["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens", "salt"],
                                      ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric", "pepper", "curry", "parsley"],
                                       ["hard cheese", "eggs", "flour", "vegetable oil"],
                                       ["potato", "eggs", "salt", "pepper", "vegetable oil"]]}
        restricted_engridients = {'onion'}
        available_ingredients = ["hard cheese", "eggs", "flour", "vegetable oil", "potato", "salt", "pepper"]
        allowed_ind = range(len(recipes['ingredients']))
        actual = ex5.filter_recipes_by_ingredients(recipes,
                                                   allowed_ind,
                                                   restricted_engridients,
                                                   available_ingredients)
        self.assertEqual([2, 3], actual)

    def test_no_dishes(self):
        recipes = {"ingredients" : [["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens", "salt"],
                                      ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric", "pepper", "curry", "parsley"],
                                       ["hard cheese", "eggs", "flour", "vegetable oil"],
                                       ["potato", "eggs", "salt", "pepper", "vegetable oil"]]}
        available_ingredients = ["hard cheese", "eggs", "flour", "vegetable oil", "potato", "salt", "pepper"]
        restricted_engridients = {'onion', 'eggs'}
        allowed_ind = range(len(recipes['ingredients']))
        actual = ex5.filter_recipes_by_ingredients(recipes,
                                                   allowed_ind,
                                                   restricted_engridients,
                                                   available_ingredients)
        self.assertEqual([], actual)

class DishesToListTestCase(unittest.TestCase):
    def test__example1(self):
        recipes = {"name": ["Kharcho soup", "Beef Shurpa", "Homemade cheese sticks", "Potato pancakes"],
                   "ingredients": [
                       ["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens", "salt"],
                       ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric", "pepper",
                        "curry", "parsley"],
                       ["hard cheese", "eggs", "flour", "vegetable oil"],
                       ["potato", "eggs", "salt", "pepper", "vegetable oil"]]
                   }
        allowed_ind = [2, 3]
        expected = ['Homemade cheese sticks - hard cheese, eggs, flour, vegetable oil', 'Potato pancakes - potato, eggs, salt, pepper, vegetable oil']
        actual = ex5.recipes_to_list(recipes, allowed_ind)

        self.assertEqual(expected, actual)


    def test__no_dishes(self):
        recipes = {"name": ["Kharcho soup", "Beef Shurpa", "Homemade cheese sticks", "Potato pancakes"],
                   "ingredients": [
                       ["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens", "salt"],
                       ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric", "pepper",
                        "curry", "parsley"],
                       ["hard cheese", "eggs", "flour", "vegetable oil"],
                       ["potato", "eggs", "salt", "pepper", "vegetable oil"]]
                   }
        allowed_ind = []
        expected = []
        actual = ex5.recipes_to_list(recipes, allowed_ind)
        self.assertEqual(expected, actual)

class MainTestCase(unittest.TestCase):
    def test_example1(self):
        ex5.russian_recipes = {"name": ["Kharcho soup", "Beef Shurpa", "Homemade cheese sticks", "Potato pancakes"],
                               "url": ["https://www.russianfood.com/recipes/recipe.php?rid=102711",
                                       "https://www.russianfood.com/recipes/recipe.php?rid=138622",
                                       "https://www.russianfood.com/recipes/recipe.php?rid=145215",
                                       "https://www.russianfood.com/recipes/recipe.php?rid=138784"],
                               "ingredients": [
                                   ["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens",
                                    "salt"],
                                   ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric",
                                    "pepper", "curry", "parsley"],
                                   ["hard cheese", "eggs", "flour", "vegetable oil"],
                                   ["potato", "eggs", "salt", "pepper", "vegetable oil"]],
                               "amount": [
                                   ["1 piece", "0.5 cups", "1 piece", "50 g", "1 piece", "1 piece", "2 spoons", "50 g",
                                    "1 spoon"],
                                   ["800 g", "8 pieces", "200 g", "150 g", "100 g", "3 pieces", "1 spoon", "0.5 spoons",
                                    "0.5 spoons", "1 spoon", "1 bunch"],
                                   ["300 g", "1 piece", "30 g", "70 ml"],
                                   ["11 pieces", "2 pieces", "0.5 spoons", "1 pinch", "1 spoon"]],
                               "time_variative": [30, 25, 15, 35],
                               "time_strict": [55, 100, 15, 30]}

        ex5.preferences = {1: "not chicken", 2: "not onion", 3: "not beef", 4: "not pepper", 5: "not butter"}

        ex5.restrictions = {"allergy sufferers": "5", "vegans": "135", "non-onion lovers": "2"}


        expected = (['Papa - onion', 'Mama - no restrictions'],
                    ['Homemade cheese sticks - hard cheese, eggs, flour, vegetable oil', 'Potato pancakes - potato, eggs, salt, pepper, vegetable oil'])
        actual = ex5.ideal_dinner(100, 5, "hard cheese", "eggs", "flour", "vegetable oil", "potato", "salt", "pepper",  Papa=["non-onion lovers"], Mama=[])

        self.assertEqual(expected, actual)


    def test_empty(self):
        ex5.russian_recipes = {"name": ["Kharcho soup", "Beef Shurpa", "Homemade cheese sticks", "Potato pancakes"],
                               "url": ["https://www.russianfood.com/recipes/recipe.php?rid=102711",
                                       "https://www.russianfood.com/recipes/recipe.php?rid=138622",
                                       "https://www.russianfood.com/recipes/recipe.php?rid=145215",
                                       "https://www.russianfood.com/recipes/recipe.php?rid=138784"],
                               "ingredients": [
                                   ["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens",
                                    "salt"],
                                   ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric",
                                    "pepper", "curry", "parsley"],
                                   ["hard cheese", "eggs", "flour", "vegetable oil"],
                                   ["potato", "eggs", "salt", "pepper", "vegetable oil"]],
                               "amount": [
                                   ["1 piece", "0.5 cups", "1 piece", "50 g", "1 piece", "1 piece", "2 spoons", "50 g",
                                    "1 spoon"],
                                   ["800 g", "8 pieces", "200 g", "150 g", "100 g", "3 pieces", "1 spoon", "0.5 spoons",
                                    "0.5 spoons", "1 spoon", "1 bunch"],
                                   ["300 g", "1 piece", "30 g", "70 ml"],
                                   ["11 pieces", "2 pieces", "0.5 spoons", "1 pinch", "1 spoon"]],
                               "time_variative": [30, 25, 15, 35],
                               "time_strict": [55, 100, 15, 30]}

        ex5.preferences = {1: "not chicken", 2: "not onion", 3: "not beef", 4: "not pepper", 5: "not butter"}

        ex5.restrictions = {"allergy sufferers": "5", "vegans": "135", "non-onion lovers": "2"}


        expected = (['Papa - onion', 'Mama - no restrictions'],
                    "Go buy ready-made food and don't suffer")
        actual = ex5.ideal_dinner(100, 5,  Papa=["non-onion lovers"], Mama=[])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
