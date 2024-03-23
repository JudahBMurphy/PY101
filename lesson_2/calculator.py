import json

LANGUAGE = 'en'

with open('calculator_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'==> {message}')

def invalid_number(user_input):
    try:
        float(user_input)
    except ValueError:
        return True
    return False

def test_input(user_input):
    while invalid_number(user_input):
        prompt(messages('invalid_number', LANGUAGE))
        user_input = input()
    return user_input


prompt(messages('welcome', LANGUAGE))

while True:
    # Ask the user for the first number.
    prompt(messages('first_number', LANGUAGE))
    first_number = test_input(input())

    # Ask the user for the second number.
    prompt(messages('second_number', LANGUAGE))
    second_number = test_input(input())

    #Ask the user for an operation to perform
    prompt(messages('operations', LANGUAGE))
    operand = test_input(input())
    while operand not in ['1', '2', '3', '4']:
        prompt(messages('bad_input_choice_4', LANGUAGE))
        operand = test_input(input())

    #Perform the operation on the two numbers
    match operand:
        case '1':
            result = float(first_number) + float(second_number)
        case '2':
            result = float(first_number) - float(second_number)
        case '3':
            result = float(first_number) * float(second_number)
        case '4':
            result = float(first_number) / float(second_number)
        case _:
            prompt(messages('bad_input', LANGUAGE))

    #Print the result to the terminal
    print(f'Result is: {result}')

    #Prompt another calculation
    prompt(messages('new_calc', LANGUAGE))
    calc_again = input()
    if calc_again and calc_again[0].lower() != 'y':
        break
    