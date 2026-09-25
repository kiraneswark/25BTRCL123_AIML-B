students = {}

while True:
    print("\n--- Attendance Tracker ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = "Not Marked"
        print("Student added!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            attendance = input("Enter P for Present or A for Absent: ")

            if attendance == "P":
                students[name] = "Present"
            elif attendance == "A":
                students[name] = "Absent"
            else:
                print("Invalid input")

        else:
            print("Student not found")

    elif choice == "3":
        print("\nAttendance:")

        for name in students:
            print(name, ":", students[name])

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        
        ##sample output
       # --- Attendance Tracker ---

#1. Add Student
#   2. Mark Attendance
#3. View Attendance
#4. Exit

#Enter your choice: 1
# Enter student name: Rahul
#Student added!

#Enter your choice: 1
#Enter student name: Priya
#Student added!

#Enter your choice: 2
#Enter student name: Rahul
#Enter P for Present or A for Absent: P

#Enter your choice: 3

#Attendance:
#Rahul : Present
#Priya : Not Marked