# try:
#     age = int(input("what is your age? "))
#     print(f"Your age is: {age}")
# except ValueError:
#     print("Please enter a valid integer for your age.")




# try:
#     food = bool(input("most girls like ice cream (True/False): "))
#     if food == True:
#         print(f" i was'nt wrong")
#     elif food == False:
#         print(f" Hummmm sounds strange")
#     else:
#         print("Please enter a valid boolean value for your food preference.")
# except ValueError:
#     print("Please enter a valid boolean value for your food preference.")



def add_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid integers for both numbers.")
add_numbers()