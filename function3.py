def greet_user():
    print("Hello user")
    print("Hello user one")
greet_user()


#                           POSITIONAL ARGUMENT
def greeting(name, level, departnemt):
    print(f"Hello {name} how are you doing. {name} is in {level} from {departnemt}")
greeting("john", "200L", "Computer Engineering")


#                           KEYWORD ARGUMENT
def greet(name, age):
    print(f"His name is {name} and he is {age} years old")
greet(name = "Jude", age = 43)


#                           GLOBAL VARIABLE
surname = "Suleman"
def sayhi():
    print(f"The guys other name is {surname}")
sayhi()

town = "Minna"
address_no = 22
school = "De-glory School"

def details():
    print(f"{school} is located at number {address_no} in the city of {town}")
details()

#                           ARGS
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add(2, 2, 1, 2, 4, 2))


#                           KWARGS
