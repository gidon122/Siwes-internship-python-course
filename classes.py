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


# class Dog:
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


class Cake:
    def __init__(self, kind, price, slices):
        self.kind = kind
        self.price = price
        self.slices = slices

    def describe(self, size):
        return f"the {self.kind} cake cost ${self.price} is divided into {self.slices} slices and the size is {size}."

instance1 = Cake("Milk", 15, 8)
instance2 = Cake("Chocolate", 20, 10)

print(instance1.describe("large"))
print(instance2.describe("medium"))