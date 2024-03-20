print('Welcome to Calculator')

# Ask the user for the first number.
print('Please enter the first number:')
first_number = int(input())

# Ask the user for the second number.
print('Please enter the second number:')
second_number = int(input())

#Ask the user for an operation to perform
print('''What operation would you like to perform?
1. Addition
2. Subtraction
3. Multiplication
4. Division''')
operand = int(input())
result = 0

#Perform the operation on the two numbers
match operand:
	case 1:
		result = first_number + second_number
	case 2:
		result = first_number - second_number
	case 3:
		result = first_number * second_number
	case 4:
		result = first_number // second_number
	case _:
		print('Input not recognized. Goodbye.')

#Print the result to the terminal
print(f'Result is: {result}')