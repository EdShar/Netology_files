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


file_name = 'recipes.txt'
print(file_to_dict(file_name))
