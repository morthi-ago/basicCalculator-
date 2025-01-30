def divisionRepete(numberOne, numberTwo):
    numberTwo = int(input('Type another number, for the divider\n'))
    print(numberOne / numberTwo)

numberOne = int(input('Type a number\n'))
numberTwo = int(input('Type another number\n'))

operation = input('What basic mathematical operation do you want to do ?\n')

if operation == '*':
    print(numberOne * numberTwo)
elif operation == '/':
    if numberTwo == 0:
        print("There isn't division by 0")
        divisionRepete(numberOne, numberTwo)
    else:
        print(numberOne / numberTwo) 
elif operation == '+':
    print(numberOne + numberTwo) 
else:
    print(numberOne - numberTwo)
    