
# Create a function that iterates each character of cpf_input. If character is a "-" or a ".", remove it

# NOTE1: if user adds characters, they should be removed from the string
# remove characters that are not numbers such as "-", and "."

def removeDots_Hyphens(cpf):
    cpf_clean_input = ""

    for q in range(len(cpf)):
        if cpf[q] == ".":
            # if character is a dot, it should not be added to cpf_input(skip)
            continue

        elif cpf[q] == "-":
            # if character is a hyphen, it should not be added to cpf_input(skip)
            continue

        else:
            cpf_clean_input += cpf[q]
    return cpf_clean_input
        

# -------------------------------------------------------------------------------------------------------------
# NOTE2: refactoring note -> if the character from the CPF is not a number, it should be removed

def remove_not_numbers(cpf):
    new_cpf = ""
    # check if each character from the cpf_input is a digit with .isDigit()
    for q in range(len(cpf)):
        if cpf[q].isdigit() == False:
            continue
        else:
            new_cpf += cpf[q]

    return new_cpf
# --------------------------------------------------------------------------------------
# Function that checks if all characters are the same

def check_if_same_number(cpf):
    if cpf.count(cpf[0]) == len(cpf):
        print(cpf, "is an invalid CPF")
        return False
    return True
