def prompt(message):
    print(f'==> {message}')

def invalid_number(user_input):
    try:
        int(user_input)
    except ValueError:
        return True
    return False

def test_input(user_input):
    while invalid_number(user_input):
        prompt("Not a valid number. Please try again.")
        user_input = input()
    return user_input


prompt('Welcome to Calculator')

# Ask the user for the first number.
prompt('Please enter the first number:')
first_number = test_input(input())

# Ask the user for the second number.
prompt('Please enter the second number:')
second_number = test_input(input())

#Ask the user for an operation to perform
print('''What operation would you like to perform?
1. Addition
2. Subtraction
3. Multiplication
4. Division''')
operand = test_input(input())
while operand not in ['1', '2', '3', '4']:
    prompt('Please choose from the given options 1, 2, 3, or 4')
    operand = test_input(input())

#Perform the operation on the two numbers
match operand:
    case '1':
        result = int(first_number) + int(second_number)
    case '2':
        result = int(first_number) - int(second_number)
    case '3':
        result = int(first_number) * int(second_number)
    case '4':
        result = int(first_number) // int(second_number)
    case _:
        print('Input not recognized. Goodbye.')

#Print the result to the terminal
print(f'Result is: {result}')
