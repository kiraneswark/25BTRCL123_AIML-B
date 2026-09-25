name = input("Enter student name: ")

marks1 = int(input("Enter marks in Subject 1: "))
marks2 = int(input("Enter marks in Subject 2: "))
marks3 = int(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)


##sample output
#Enter student name: koushik
#Enter marks in Subject 1: 99
#Enter marks in Subject 2: 98
#Enter marks in Subject 3: 100

#Student Name: koushik
#Total Marks: 297
#Average: 99.0
#Grade: A