def file_to_dict(name_file):
    cook_book = {}

    with open(name_file, 'rt', encoding='UTF-8') as file:
        for dish in file:
            ingredients_count = int(file.readline())
            ingredients_list = []
            for ingredient in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish.strip()] = ingredients_list

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    book_dict = file_to_dict(file_name)
    shop_list = {}

    for dish in dishes:
        for ingredient in book_dict.get(dish):
            if ingredient.get('ingredient_name') not in shop_list:
                shop_list[ingredient.get('ingredient_name')] = {'measure': ingredient.get('measure'),
                                                                'quantity': int(
                                                                    ingredient.get('quantity')) * person_count}
            else:
                shop_list[ingredient.get('ingredient_name')] = {'quantity':
                                                                    int(shop_list.get(
                                                                        ingredient.get('ingredient_name')).get(
                                                                        'quantity')) + int(
                                                                        ingredient.get('quantity')) * person_count}

    return shop_list


file_name = 'recipes.txt'
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
