#Assuming you are living until 90 years old.
age = input("What is your current age? ")

#Variable is 90, transform input from string to integer.
total = 90 - int(age)

#Create three variables for days, weeks, months.
days = total * 365
weeks = total * 52
months = total * 12

#Print the result and use a f-string
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
