#              INDEXING

# Msg = "photosynthesis"

# print (Msg[0:-1])
# print (Msg[2:4])
# print (Msg[6:])
# print (Msg[:4])
# print (Msg[:])

# name = "Christopher"
# print(name[1:-1])

#               FORMATTED STRINGS
# first_name = "John"
# last_name = "Smith"
# age = 39

# Message = first_name + last_name + " is a Senior Developer and he just turned " + str(age) 

# Message = f"Mr. {first_name} {last_name} is a Senior Java Developer and he just turned {age}" 
# print (Message)

# name = input("What is your name? ")
# color = input("What is your favourite color ")
# print (f"{name} favourite color is {color}")


#               STRING LEGNTh
# course = "Python course"
# print (len(course))

#                class exercise on string legth
# name = input("what is your name ")
# no_of_char = len(name)
# char = f"your name has {no_of_char} character"
# print (char)

# DOT OPERATOR

# name = "HELLO CHAMPS"
# print (name.upper())

# note = "it's a good day"
# print(note.find('i'))
# print (note.replace('good', 'very good'))

#       ASSIGNMENT

#PLATFORM THAT FILTERS WORDS
msg = input("say something: ")
last = (msg.lower())
print (last.replace('fish', '***'))

# UNIVERSITY SYSTEM FOR COLLECTING STUDENT DETAILS
name = input("What is your name? ")
age = int(input("What is your age? "))
gender = input("What is your gender? ")
department = input("What is your department? ")
matric_no = input ("What is your Matriculation numbert? ")
student_details = f"THE STUDENT DETAILS ARE:\nName: {name}\nAge: {age}\nGender: {gender}\nCourse: {department}\nMatric no: {matric_no}"
print (student_details)