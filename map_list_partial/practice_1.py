from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# print(produtos)
# print_iter(produtos)

# goal: increase prices in 10%

# A function that increases prices in 10%

def increase_preco_percent( value , percent):
    return round(value * percent, 2)

# Using partial()

increase_preco_w_partial = partial(increase_preco_percent, percent = 1.1)

# With list comprehension
# new_produtos = [{**p, "preco": increase_preco_w_partial(p["preco"])} for p in produtos]

# Using Map function
# map "passes by" each element of the list
# and executes the function provided as parameter
# this function has the element from the list as the 
# parameter

def change_price(product):
    return {**product, "preco": increase_preco_w_partial(product["preco"]) }

new_produtos = list(map(change_price, produtos))


print(new_produtos)



