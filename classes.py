#                           IT RAN
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("moving")
#     def stop(self):
#         print("stopping")
# leave = Point(10, 20)
# leave.move()
# leave.stop()


#                           IT RAN
#  class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"{self.name} is barking.")
#     def sit(self):
#         print(f"{self.name} is sitting.")
#     def getage(self):
#         print(f"{self.name} is {self.age} years old.")
# Dog1 = Dog("Buddy", 3)
# Dog1.bark()
# Dog1.sit()
# Dog1.getage()


#                           IT RAN
#  class Cake:
#     def __init__(self, kind, price, slices):
#         self.kind = kind
#         self.price = price
#         self.slices = slices

#     def describe(self, size):
#         return f"the {self.kind} cake cost ${self.price} is divided into {self.slices} slices and the size is {size}."

# instance1 = Cake("Milk", 15, 8)
# instance2 = Cake("Chocolate", 20, 10)

# print(instance1.describe("large"))
# print(instance2.describe("medium"))



#                           IT RAN
#  class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display(self):
#         return (
#             f"I saw a great book titled '{self.title}'. It was authored by {self.author}. It revealed so much insight into the power of the mind. It cost ${self.price}."
#         )
# group1 = Book("Think and Grow Rich", "Dele Dam", 1400)
# print(group1.display())



#                           IT DID'NT RUN
#  class student:
#     def __init__(self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level

#     def introduce(self, staff):
#         return f"I am {self.name} a student of {self.course} department, i am in {self.level}L, really nice to meet you. i love Mr{self.staff}"

# student1 = student("Ada James", "Biochemistry", 200)

# print(student1.introduce("Dr Bala"))



#                             IT DID'NT RUN
# class Rectagle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print(f"{self.length*self.width}")
#     def perimeter(self):
#         print(f"{self.length+self.width}")
# Rectagle1 = Rectagle(34, 54)
# Rectagle1.area()
# Rectagle1.perimeter()



class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print(f"{self.owner} just deposited some amount of money. total assets is ${self.balance}")
    def withraw(self):
        print(f"Hello {self.owner} you just made some transactions. total assets is now ${self.balance}")
    def check(self):
        print(f"your total asset is ${self.balance}. Thanks for banking with us")
Bank1 = Bank("Aliu Ahmed", 190243.32)
Bank1.deposit()
Bank1.withraw()
Bank1.check()