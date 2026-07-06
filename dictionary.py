digit_mapping = {
    "1" : "One", 
    "2" : "two", 
    "3" : "three", 
    "4" : "four", 
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero",}
phone = input("what is your phone number? ")
for char in phone:
    result = digit_mapping.get(char, "!")
    print(result)