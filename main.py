# This is a sample Python script.

#level beginner logic building project
#project: student study & grade managment system
#the program should allow a user to:
#Enter a students name and information
#enter quiz score
#calculate the avarage scire
#determine whether student assed ir failed
#store subjects and grades
#display a report
#ask user whether they want to add another student

passed_value= 0
student_score= []
student_address = []
data_1 = input("Student's name, please: ")
while len(data_1) > 20:
    print("Student's name is too long.")
    data_1 = input("Student's name, please: ")
    student_address.append(data_1)
data_2 = int(input("Student's age, please: "))


while data_2 <= 15:
    print("Student's age must be greater than or equal to 15")
    data_2 = int(input("Student's age, please: "))
    student_address.append(data_2)

data_3 = int(input("Student's ID, please: "))
while data_3 <=0:
    print("Student's ID must be positive")
    data_3= int(input("Student's ID, please: "))
    student_address.append(data_3)

for score in range(4):
    student_scor = int(input("Student's score, please: "))
    student_score.append(student_scor)
    passed_value = passed_value + student_scor
average_passed_value = passed_value / 4

print("Your average score is: ", average_passed_value)
print("Your score is: ", student_score)
if average_passed_value >= 80:
    print("Excellent")
elif average_passed_value >= 50:
    print("you are passed")
else:
    print("you are failed")

