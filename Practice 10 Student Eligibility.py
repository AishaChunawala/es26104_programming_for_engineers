#A student is eligible when marks are at least 50 AND attendance is at least 75%. Also demonstrate OR and NOT.

marks = int(input("Enter marks: "))

attendance = int(input("Enter attendance percentage: "))

marks_ok = marks >= 50

attendance_ok = attendance >= 75

eligible = marks_ok and attendance_ok

one_condition = marks_ok or attendance_ok

not_eligible = not eligible

print("AND =", eligible)

print("OR =", one_condition)

print("NOT =", not_eligible)