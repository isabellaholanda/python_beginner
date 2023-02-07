student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# can't use len() or sum()
sum_of_heights = 0
num_students = 0
for heights in student_heights:
    sum_of_heights += heights
    num_students += 1

average = sum_of_heights / num_students
print(round(average))
