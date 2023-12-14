import re

# russian_recipes = {"name" : ["Kharcho soup", "Beef Shurpa", "Homemade cheese sticks", "Potato pancakes"],
#                    "url" : ["https://www.russianfood.com/recipes/recipe.php?rid=102711",
#                             "https://www.russianfood.com/recipes/recipe.php?rid=138622",
#                             "https://www.russianfood.com/recipes/recipe.php?rid=145215",
#                             "https://www.russianfood.com/recipes/recipe.php?rid=138784"],
#                    "ingredients" : [["chicken", "rice", "garlic", "butter", "onion", "carrot", "tomato paste", "greens", "salt"],
#                                     ["beef", "potato", "carrot", "onion", "sweet pepper", "bay leaf", "salt", "turmeric", "pepper", "curry", "parsley"],
#                                     ["hard cheese", "eggs", "flour", "vegetable oil"],
#                                     ["potato", "eggs", "salt", "pepper", "vegetable oil"]],
#                    "amount" : [["1 piece", "0.5 cups", "1 piece", "50 g", "1 piece", "1 piece", "2 spoons", "50 g", "1 spoon"],
#                                ["800 g", "8 pieces", "200 g", "150 g", "100 g", "3 pieces", "1 spoon", "0.5 spoons", "0.5 spoons", "1 spoon", "1 bunch"],
#                                ["300 g", "1 piece", "30 g", "70 ml"],
#                                ["11 pieces", "2 pieces", "0.5 spoons", "1 pinch", "1 spoon"]],
#                    "time_variative" : [30, 25, 15, 35],
#                    "time_strict" : [55, 100, 15, 30]}
#
# preferences = {1 : "not chicken",   2 : "not onion",  3 : "not beef",  4 : "not pepper", 5 : "not butter"}
#
# restrictions = {"allergy sufferers" : "5",  "vegans" : "135",  "non-onion lovers" : "2"}


def ideal_dinner(max_time, n_members, *available_ingredients, **family_kwargs):
    output_family, restricted_ingredients = get_outfamily_and_restricted_ingredients(preferences,
                                                                           restrictions,
                                                                           family_kwargs)

    recipe_ind = list(range(len(russian_recipes['name'])))
    recipe_ind = filter_recipes_by_time(russian_recipes,
                                        recipe_ind,
                                        max_time,
                                        n_members)
    recipe_ind = filter_recipes_by_ingredients(russian_recipes,
                                              recipe_ind,
                                              restricted_ingredients,
                                              available_ingredients)
    output_recipes = recipes_to_list(russian_recipes, recipe_ind)
    if not output_recipes:
        output_recipes = "Go buy ready-made food and don't suffer."

    return output_family, output_recipes




def get_outfamily_and_restricted_ingredients(preferences, restrictions, family_kwargs):
    preferences = rework_preferences(preferences)
    output_family = []
    restricted_ingredients = set()

    for role, pref_list in family_kwargs.items():
        role_restricted = []
        for category in pref_list:
            excluded_ids = restrictions[category]
            for _id in excluded_ids:
                _id = int(_id)
                ingredient = preferences[_id]
                role_restricted.append(ingredient)
                restricted_ingredients.add(ingredient)
        if role_restricted:
            role_str = f"{role} - {', '.join(role_restricted)}"
        else:
            role_str = f"{role} - no restrictions"
        output_family.append(role_str)
    return output_family, restricted_ingredients


def rework_preferences(preferences):
    return {key: re.findall(r'^not\s(.+)', value)[0]
            for key, value in preferences.items()}


def filter_recipes_by_time(recipes, allowed_inds, max_time, n_members):
    filtered_inds = []
    for ind in allowed_inds:
        variative = recipes['time_variative'][ind]
        strict = recipes['time_strict'][ind]
        total = round(variative / n_members, 4) + strict
        if total <= max_time:
            filtered_inds.append(ind)
    return filtered_inds


def filter_recipes_by_ingredients(recipes,
                                  allowed_inds,
                                  restricted_ingredients,
                                  available_ingredients):
    filtered_inds = []
    for ind in allowed_inds:
        ingredients = recipes['ingredients'][ind]
        for ingredient in ingredients:
            if (ingredient in restricted_ingredients or
                    ingredient not in available_ingredients):
                break
        else:
            filtered_inds.append(ind)
    return filtered_inds


def recipes_to_list(recipes, allowed_inds):
    res_list = []
    for ind in allowed_inds:
        name = recipes['name'][ind]
        ingredients = recipes['ingredients'][ind]
        string = f"{name} - {', '.join(ingredients)}"
        res_list.append(string)
    return res_list


if __name__ == '__main__':
    ideal_dinner(100, 5)