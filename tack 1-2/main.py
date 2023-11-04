import os
from pprint import pprint


# Функция ч_1 задания. Создание словаря блюд
def cook_book_read():
    cook_book = {}
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n\n')
        for dish in data:
            dish = dish.split('\n')
            ingrdns_all = []
            for ingr in dish[2:]:
                ingrdns = {}
                ingrdns['ingredient_name'], ingrdns['quantity'], ingrdns['measure'] = ingr.split('|')
                ingrdns['quantity'] = int(ingrdns['quantity'])
                ingrdns_all.append(ingrdns)
            cook_book[dish[0]] = ingrdns_all
    return cook_book


cook_book = cook_book_read()
pprint(cook_book)


# Функция ч_2 задания. Создание словаря ингредиентов
def get_shop_list_by_dishes(dishes, person_count):
    ingrs_list = {}
    for dish_name in dishes:
        for ingr in cook_book[dish_name]:
            dict_ingrs = {}
            if ingr['ingredient_name'] not in ingrs_list:
                dict_ingrs['measure'] = ingr['measure']
                dict_ingrs['quantity'] = ingr['quantity'] * person_count
                ingrs_list[ingr['ingredient_name']] = dict_ingrs
            else:
                ingrs_list[ingr['ingredient_name']]['quantity'] = ingrs_list[ingr['ingredient_name']]['quantity'] + \
                                                                  ingr['quantity'] * person_count
    return ingrs_list


pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Омлет'], 2))


