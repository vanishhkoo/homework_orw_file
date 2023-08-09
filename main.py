# recipes_open = open('recipes.txt')
# print(recipes_open.read())

cook_book = {}

with open('recipes.txt', 'rt') as recipes_file:
    for recipes in recipes_file:
        recipes_name = recipes.strip()
        recipes_list = []
        recipes_count = recipes_file.readline()
        for x in range(int(recipes_count)):
            rcps_count = recipes_file.readline()
            ingredient_name, quantity, measure = rcps_count.strip().split(' | ')
            recipes_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book_recipes = {recipes_name: recipes_list}
        y = recipes_file.readline()
        cook_book.update(cook_book_recipes)
print(cook_book)



