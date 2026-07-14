#       VALUE ERROR
# try:
#     a = int(input("input first value"))
#     b = int(input("input second number"))

#     c = a + b
#     print(c)
# except ValueError:
#     print("enter a number please")


#       ZERODIVISIONERROR

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Can't divide by zero")


# try:
#     number = int(input("enter a number "))
#     print(100 / number)
# except ValueError:
#     print("enter a valid number")
# except ZeroDivisionError:
#     print("you cant divide by zero")


# try:
#     a = int(input("enter first number "))
#     b = int(input("enter second number "))
#     c = a/b
#     print(c)
# except ValueError:
#     print("Enter a correct value")
# except ZeroDivisionError:
#     print("You cannot didve by zero")
# else:
#     print("Thank you for banking with us")


def calculator(a, b, opt):
    # a = int(input("enter a number "))
    # b = int(input("enter a number "))
    # opt = input("enter an operation")
    if opt == "+":
        return a + b
    elif opt == "-":
        return a - b
    elif opt == "/":
        return a / b
    elif opt == "*":
        return a * b
    else:
        return("none")


print(calculator(22, 12, "-"))