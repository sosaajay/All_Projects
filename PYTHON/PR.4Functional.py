print()
print("welcome to the our school student marks analysis system😇:")
print()
marks = [65, 78, 98, 45, 32, 87, 21, 90, 66, 72, 33, 88, 56, 77, 43, 61, 85, 49, 69, 74]

total_students = len(marks)
highest = max(marks)
lowest = min(marks)
average = sum(marks) / total_students

passed = len([m for m in marks if m >= 35])
failed = total_students - passed
pass_percentage = (passed / total_students) * 100

sorted_marks = sorted(marks)

grade_a = len([m for m in marks if m >= 85])
grade_b = len([m for m in marks if 70 <= m < 85])

print(f"Total Students: {total_students}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.1f}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass Percentage: {pass_percentage:.1f}%")
print(f"Sorted Marks: {sorted_marks}")
print(f"Grade A: {grade_a} Students")
print(f"Grade B: {grade_b} Students")

print("....:")

print("thank you for using our school student marks analysis system:🫡")

print()