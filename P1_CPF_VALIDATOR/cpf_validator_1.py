# 1. Import functions from function.py file from the same folder

from functions import remove_not_numbers, check_if_same_number

# ----------------------------------------------------------------------------------------------------
# 2. input of CPF (string)
cpf_input = input("Insert your CPF: ") 

# ----------------------------------------------------------------------------------------------------

# 3. Clean the CPF input
cpf = remove_not_numbers(cpf_input)

# 4. Define an array containing numbers from 10 to 2
ten_to_2_arr = [10,9,8,7,6,5,4,3,2]





# 5. Input Validation 

# - Check length of cpf variable
result = 0
if len(cpf) == 11:
    n = 0 # to iterate cpf array and the ten_to_2_arr
    while n < len(ten_to_2_arr) :
        cpf_input_int = int(cpf[n])
        result += cpf_input_int * ten_to_2_arr[n]
        n +=1

# Multiply by 10 and divide by 11 and take the remainder.
# Compare the remainder with the first digit 
remainder = (result * 10) % 11

    # Important OBS: If the remainder is almost 10 (9.1 for example), it should return 0, not 10
if remainder > 9 :
    remainder = 0

    # 6. Confirm if it's a valid CPF or not valid

    # 6.1. Consider the Special Cases

    # When all the characters from the CPF are equal
    # To check if all the characters are equal by iterating cpf
    # Logic: if the frequency that the first character appeared is equal to the length of the cpf, it means
    # the all the characters from the cpf are the same which makes the cpf not valid

# First, check if all numbers are the same. If not, it will be invalid. If so, they check if the remainder is
# the same as the first digit of the CPF (cpf[9])
if check_if_same_number(cpf):

    if str(remainder) == cpf[9]:
        print(cpf, " is a valid CPF")

    else:  
        print(cpf, " is not a valid CPF")


    









    



        

    


