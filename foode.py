recipes = {
    'potato': 'a basic mash',
    'potato,': 'a basic mash',
    'potato butter cheese': 'a classic mash',
    'potato oil': 'chips',
    'flour eggs milk sugar butter': 'basic cake',
    'olive oil leek sausage rice': 'seafood rice'
}

dir = {
    'a basic mash': 'Get your potato and mash it with a masher until it looks like mash. Then cook the mash.',
    'a classic mash': 'Get your potato and mash it with a masher until it looks like mash.\nThen add butter and cheese. After this, cook the mash with cheese.',
    'chips': 'Get your potato and cut it with a knife into strips. Then cook the strips in oil.',
    'basic cake': 'Mix your eggs and sugar thoroughly. After this, add the flour and mix well.\nIn another bowl, mix the milk and eggs together. Add the wet mixture to the dry mixture and mix it into batter.\nBake for 20-25 minutes.'
}

def scan():
    """
    Scans available ingredients and suggests possible recipes.
    """
    ingredients = input('What ingredients do you have at your disposal?\n').lower()
    possible_recipes = []

    for key, recipe in recipes.items():
        # Check if all ingredients for a recipe are in the user's input
        if all(ingredient in ingredients for ingredient in key.split()):
            possible_recipes.append(recipe)

    if possible_recipes:
        print('You can cook:', ', '.join(set(possible_recipes)))
    else:
        print("No matching recipes found.")

def learn():
    """
    Provides the instructions for a chosen recipe.
    """
    recipe_name = input('What recipe do you want to learn?\n').strip()
    if recipe_name in dir:
        print(f'To cook "{recipe_name}", follow these steps:', dir[recipe_name], sep='\n')
    else:
        print("Recipe not found.")

# Example usage: