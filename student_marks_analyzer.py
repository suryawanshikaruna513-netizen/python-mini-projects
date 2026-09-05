# Student Marks Analyzer

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")