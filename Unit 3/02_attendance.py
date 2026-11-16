n = int(input("Enter number of students: "))
attendance = []
for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ")
    attendance.append([name, status])
print("\nAttendance:")
for student in attendance:
    print(student[0], "-", student[1])