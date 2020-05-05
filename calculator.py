""" Simple calculator program """

"""functions of Operators"""


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


"""functions of Operators"""


print("Select the operation- \n"
      "1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n")

select = int(input("Select the operation from  1, 2, 3, 4 :"))

number1 = float(input("Enter the first number :"))
number2 = float(input("Enter the second number :"))

if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))

elif select == 2:
    print(number1, "+", number2, "=", sub(number1, number2))

elif select == 3:
    print(number1, "+", number2, "=", mul(number1, number2))

elif select == 4:
    print(number1, "+", number2, "=", div(number1, number2))

else:
    print("Invalid Operator")
