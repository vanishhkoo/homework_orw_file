# recipes_open = open('recipes.txt')
# print(recipes_open.read())



with open('recipes.txt', 'rt') as recipes_file:
    cook_book = {}
    for recipes in recipes_file:
        recipes_name = recipes.strip()
        recipes_list = []
        recipes_count = recipes_file.readline()
        for x in range(int(recipes_count)):
            ingredient_name, quantity, measure = recipes_file.readline().strip().split(' | ')
            recipes_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        recipes_file.readline()
        cook_book[recipes_name] = recipes_list
# print(cook_book)

def get_shop_list_by_dishes(dishes, person):
    for dish in dishes:
        for x in cook_book:
            if x == dish:
                dish_all_persons = quantity * person
                print(dish)
            # else:
                # print('There is no such dish')

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




