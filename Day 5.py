# #           MODULE



# # import math

# # print (math.ceil(3.8))
# # print(math.floor(3.8))





# # weight = float(input("what is your weight in KG? "))
# # height = float(input("what is your height in cm? "))
# # bmi = weight / (height ** 2)
# # print ("Your BMI is:", bmi)


# #           CONDITIONAL STATEMENT

# # is_hot = True
# # is_cold = True

# # if is_hot:
# #     print("it is a hot day")
# #     print("Drink plenty of water")

# # elif is_cold:
# #     print("It is a cold day")
# #     print("Wear a warm cloth")

# # else:
# #     print("It is a lovely day")

# # print("Enjoy your day")

# tmp = input("what is the temperature outside(hot/cold)? ").lower

# if tmp == "hot":
#     print("it is a hot day")
#     print("drink plenty of water")

# elif tmp == "cold":
#     print("it is a cold day")
#     print ("wear warm clothes")

# else:
#     print("it is a lovely day")



total_age = 115
total_days_in_age = total_age * 365
total_weeks_in_age = total_age * 52
total_months_in_age = total_age * 12

age = int(input("how old ar you? "))
days = total_days_in_age - (age * 365)
weeks = total_weeks_in_age - (age * 52)
months = total_months_in_age - (age * 12)

print(f"You have {days} days, {weeks} weeks, {months} months left")