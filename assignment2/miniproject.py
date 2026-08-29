
print("------ STUDENT GRADING SYSTEM ------")

name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

if marks >= 90:
    grade = "A"

elif marks >= 80:
    grade = "B"

elif marks >= 70:
    grade = "C"

elif marks >= 60:
    grade = "D"

elif marks >= 40:
    grade = "E"

else:
    grade = "Fail"

print("\n------ RESULT ------")
print("Student Name :", name)
print("Marks        :", marks)
print("Grade        :", grade)
print("--------------------")

#sample output
#------ STUDENT GRADING SYSTEM ------
#Enter Student Name: kiran
#Enter Marks: 80

#------ RESULT ------
#Student Name : kiran
#Marks        : 80.0
#Grade        : B
#--------------------