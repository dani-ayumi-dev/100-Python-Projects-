list_of_numbers = [1,2,3,4]

#goal: create another list with triple version of each element of list_of_numbers

# With map

# new_list = list(map(lambda n:n * 3, list_of_numbers))


# Create a function that triplicate the numbers

# def triplicate(number):
#     return number * 3

# new_list = list(map(triplicate, list_of_numbers))


# with list comprehension

new_list = [n * 3 for n in list_of_numbers]
print(new_list)

