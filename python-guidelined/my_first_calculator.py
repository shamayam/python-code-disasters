# my_first_calculator.py by AceLewis
from numpy import nan


class Calculator:
    """
    Calculator allowing the functions add, subtract, multiply and divide
    """
    def __init__(self):
        print('Welcome to this calculator!')
        print('It can add, subtract, multiply and divide numbers')
        self.num1 = 0
        self.num2 = 0

    def add(self):
        return num1 + num2

    def subtract(self):
        return num1 - num2

    def multiply(self):
        return num1 * num2

    def divide(self):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Divide by 0 error, please try a different value")
            return nan

    def calculate(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        if sign == '+':
            return self.add()
        if sign == '-':
            return self.subtract()
        if sign == '*':
            return self.multiply()
        if sign == '/':
            return self.divide()
        print(f'The {sign} was not one of +, -, *, /. Please try again.')


if __name__ == '__main__':
    calculator = Calculator()

    # this variable keeps track of whether or not we should continue running the calculator
    cont = ''
    while cont != 'q':
        num1 = int(input('Please choose your first number: '))
        sign = input('What do you want to do? +, -, /, or *: ')
        num2 = int(input('Please choose your second number: '))
        print(num1, sign, num2, '=', calculator.calculate(num1, num2, sign))

        cont = input('Press q + enter to quit, enter to continue: ')
    print("Thanks for using this calculator, goodbye :)")
