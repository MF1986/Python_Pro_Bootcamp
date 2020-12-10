print("Welcome to the tip calculator")

#make the input from bill as a float
bill = float(input("What was the total bill? $"))

#choose a percentage as an integer
tip = int(input("what percentage tip would you like to give? 10, 12 or 15? "))

#split the bill by X people
ppl = int(input("How many people to split the bill? "))

#calcul the tip to the bill
tip_bill = tip / 100 * bill + bill

#print the result and round to two decimals
print(f"each person should pay: {round(tip_bill/ppl,2)}")
