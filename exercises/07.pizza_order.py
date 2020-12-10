print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Create a variable bill with amount 0.
bill = 0


#Input size will increase the bill.
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
 
#Pepperoni small price on small size.
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
#Extra cheese is the same price on all size.
if extra_cheese == "Y":
  bill += 1

print(f"Your pizza will cost ${bill}")
