height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#New variable 'a' as a float
a = float(height)

#New variable 'b' as an integer
b = int(weight)

#Print integer (weight - height on power 2).
print(int(b/a**2))
