import json

with open('calculator_messages.json','r') as file:
    MESSAGES = json.load(file)

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
        prompt(MESSAGES['invalid_number'])
        user_input = input()
    return user_input


prompt(MESSAGES['welcome'])

while True:
    # Ask the user for the first number.
    prompt(MESSAGES['first_number'])
    first_number = test_input(input())

    # Ask the user for the second number.
    prompt(MESSAGES['second_number'])
    second_number = test_input(input())

    #Ask the user for an operation to perform
    prompt(MESSAGES['operations'])
    operand = test_input(input())
    while operand not in ['1', '2', '3', '4']:
        prompt(MESSAGES['bad_input_choice_4'])
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
            prompt(MESSAGES['bad_input'])

    #Print the result to the terminal
    print(f'Result is: {result}')

    #Prompt another calculation
    prompt(MESSAGES['new_calc'])
    calc_again = input()
    if calc_again and calc_again[0].lower() != 'y':
        break
    