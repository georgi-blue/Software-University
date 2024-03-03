def cookbook(*recipes):
    cuisine_dict = {}

    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(cuisine_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result_output = ""
    for cuisine, recipes in sorted_cuisines:
        result_output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        recipes_sorted = sorted(recipes, key=lambda x: x[0])
        for recipe_name, ingredients in recipes_sorted:
            result_output += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result_output.strip()

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzareella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))


