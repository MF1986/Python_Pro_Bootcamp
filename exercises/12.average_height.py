#Forbidden to use SUM & LEN.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#initialize the first list
total_heights = 0

#Create a loop function
for height in student_heights:
  total_heights += height
print(total_heights) 

#initialize the second list
number_of_students = 0

#create a loop function
for student in student_heights:
  number_of_students += 1
print(number_of_students)

#Average
average_height = round(total_heights / number_of_students)
print(average_height)
