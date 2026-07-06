# def party_entry(age):
#     if age < 18:
#         print("you cant go in you are underage")
#     elif age > 18:
#         print("You can go in")
# party_entry(22)


def check(gender, age):

    if gender == "male":
        print("use door A")
        if age < 0:
            print("Your are not serious")
        elif age <= 12:
            print("Sit in front row")
        else:
            print("Sit in the back row")
    elif gender == "female":
        print("use door B")
        if age < 0:
            print("Your are not serious")
        elif age <= 12:
            print("Sit in front row")
        else:
            print("Sit in the back row")
    else:
        print("input a proper gender")

check("male", 10)