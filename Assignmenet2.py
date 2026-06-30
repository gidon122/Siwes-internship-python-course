# temp = int(input("what is the temperature in Celsius? "))

# if temp >= 35:
#     print("It is a hot day, Wear some light clothes and drink plenty of water")
# if temp <= 20:
#     print("It is a cold day, wear warm clothes")
# else:
#     print("It is a lovely day")


# i = 3
# while i <= 5:
#     print(i)
#     i += 1
# print("Done")


# secret_number = 3
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Make a guess (1 to 9) "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won")
#         break
#     else:
#         print("Try again")
# print(f"The secrete_number was {secret_number} ")


# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.append(18)
# numbers.remove(1)
# numbers.pop()
# numbers.clear()
# numbers.insert(0, 21)
# numbers.extend([9,19, 20])
# print (numbers)


# nums = [2, 4, 7, 5, 3, 8, 6]
# ups = downs = 0
# for i in range(1, len(nums)):
#     if nums[i] > nums[i-1]


# num =[1, 5, 7, 2, 7, 8]
# up = 0
# down = 0
# max_jump = 0
# for i in range(len(num)):
#     c = num[i]
#     nn = i+1
#     if c < nn:
#         up += 1
#     elif c > nn:
#         down += 1
#     else:
#         equal += 1
    
#     if c > nn:
#         jump = c - nn
#     elif c < nn:
#         jump =nn - c

#     else:
#         jump = 0

#     if jump > max_jump:
#         max_jump = jump

# print(up, down, max_jump)

numbers = [1, 2, 21, 4, 5, 6, 7, 8]
numbers.pop()
print(numbers)
print(numbers.pop())
a = numbers.pop()
print(40 - a)