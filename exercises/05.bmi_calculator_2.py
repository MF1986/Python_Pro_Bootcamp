height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#weight divided by height on power 2
bmi = round(weight/height**2)


#Conditions if/elif/else for BMI.

if bmi < 18.5:
  print(f"Your BMI is {bmi} you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi} you have a normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi} you are overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi} you are obese.")
else:
  print(f"Your BMI is {bmi} you are clinically obese.")
