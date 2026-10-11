# CPF Validator with Python

## The project

|Feature| Link to the code|
|----|-----------------|
|Validate 1st digit of the CPF|![validate first digit](cpf_validator_1.py)|
|Validate 2nd digit of the CPF|![validate second digit](cpf_validator_2.py)|
|Functions|![Important Functions](functions.py)|

## Description

Python validator validates CPF (Brazilian Tax ID) following a simple algorithm provided by the Brazilian Government. 

## The code

### Functions.py 
The most important part of the project are the functions that can be reused throughout the code. They are:

- remove_not_numbers(cpf) ---> removes every character that is not a number 
- check_if_same_number(cpf) ---> removes CPFs a set of 11 numbers that are the same (ex. 111.111.111-11)

Function that was created but not used:
- removeDots_Hyphens(cpf) ---> removes only dots and hyphens 

### Validate first digit after "-"
````python
P1_CPF_VALIDATOR/cpf_validator_1.py
````



### Validate second digit after "-"

````python
from functions import remove_not_numbers, check_if_same_number
  
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
    while i < len(cpf) - 1: # len(cleaned_cpf) = 11
        cpf_char_to_number = int(cpf[i])
        
        result += cpf_char_to_number * array_11_to_2[i]

        i+= 1

    # 4. multiply the result by 10 and divide by 11. Find the remainder

    remainder = (result * 10) % 11

    # 5. Compare the remainder with the CPF second digit after "-"

    if check_if_same_number(cpf):

        if remainder == int(cpf[10]):
            print("CPF: ", cpf, "is valid")

        else:   
            print("CPF: ", cpf, "is invalid")
else:
    print(cpf, " has additional digits")

````

## Outputs

Example of valid CPFs:
- 034.994.490-30
- 29416066028
- 294.160.660----------------------------------------------------------------28

#### Checking 034.994.490-30
1st digit:
![Checking First Digit](assets\checking_valid_cpfs\checking_valid_inputs_034.994.490-30.gif)

*Note about this validation:*
Before testing the code with CPF 034.994.490-30, I noticed that the first digit validator output was positive, however, when testing the second digit validator, the output was negative. Reason: the remainder was equalling 10, which will always give a negative output since cpf[9] can't reach a number higher than 9.

2nd digit:
![Checking Second Digit](assets\checking_valid_cpfs\P1_CPF_VALIDATOR\assets\checking_valid_cpfs\checking_valid_inputs_034.994.490-30_second_digit.gif)



#### Checking 29416066028
1st digit:
![Checking First Digit](assets\checking_valid_cpfs\checking_valid_inputs_29416066028_first_digit.gif)

2nd digit:
![Checking Second Digit](assets\checking_valid_cpfs\checking_valid_inputs_29416066028_second_digit.gif)


Example of invalid CPFs:
- 111.111.111-11
- 22222222222
- 23466724313


#### Checking 29416066028
1st digit:
![Checking First Digit](assets\checking_valid_cpfs\checking_valid_inputs_111.111.111-11_first_digit.gif)

2nd digit:
![Checking Second Digit](assets\checking_valid_cpfs\checking_valid_inputs_111.111.111-11_second_digit.gif)




## Tools used
- Python language:
    - Loop;
    - Functions.


## Conclusion

This project validates the first and the second digits of a CPF by calculating each iterated number. For that, I had to work with type coercion, loops, and input validation.