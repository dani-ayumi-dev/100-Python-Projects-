from functions import remove_not_numbers, check_if_same_number

# 222.222.222-22
  

# VALIDATE THE SECOND DIGIT OF THE CPF

# 1. Insert the CPF inpuT

cpf_input = input("Insert CPF: ")

# 2. Clean CPF input with function

cpf = remove_not_numbers(cpf_input)

# 3. Multiply the first 9 digits of the cpf by each element of an array that starts with 11 and ends with 2]

array_11_to_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

i = 0
result = 0
if len(cpf) == 11:
    while i < len(cpf) - 1: # len(cpf) = 11
        cpf_char_to_number = int(cpf[i])
        
        result += (cpf_char_to_number * array_11_to_2[i])

        i += 1

# 4. multiply the result by 10 and divide by 11. Find the remainder

remainder = (result * 10) % 11

# Important OBS: If the remainder is10, it should equal 0, not 10
if remainder > 9:
    remainder = 0


# 5. Compare the remainder with the CPF second digit after "-"

if check_if_same_number(cpf):

    if remainder == int(cpf[10]):
        print("CPF: ", cpf, "is valid")

    else:   
        print("CPF: ", cpf, "is invalid")
else:
    print(cpf, " has additional digits")










