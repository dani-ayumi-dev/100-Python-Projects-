from functools import partial

def print_iteration(iterator):
    print(*list(iterator), sep = "\n")
    print()

# CHALLENGE: Create a funcion that changes the key of the dict 

# (use: partial and map)

animals = [
    {"animal": "butterfly", "color": "yellow", "legs": 6},
    {"animal": "ant", "color": "black", "legs": 6},
    {"animal": "spider", "color": "brown", "legs": 8},
    {"animal": "bee", "color": "yellow", "legs": 6},
    {"animal": "ladybug", "color": "red", "legs": 6},
    {"animal": "grasshopper", "color": "green", "legs": 6},
    {"animal": "scorpion", "color": "black", "legs": 8},
    {"animal": "dragonfly", "color": "blue", "legs": 6},
]

# create a function that does the replacement of keywords

def replacing(key ,old_key, new_key):
    return key.replace("animal", "insect")

# Adding this function to partial

replacing_with_partial = partial(replacing, old_key = "animal", new_key = "insect")
# Create a function that receives animals (iterator) and iterates through it to change the keywords

def change_key(iterator):
    return {replacing_with_partial(key): value  for key, value in iterator.items()} 
        
    # {replacing_with_partial(key): value for key, value in iterator.items()}

    


# trying with mapping

animals_mapped = map(change_key, animals)

print_iteration(animals_mapped)




