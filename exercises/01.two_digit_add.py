#Type a two digit number which will be stored in the variable two_digit_number.
two_digit_number = input("Type a two digit number: ")

#Digit are still in string, convert it to integer and keep only the first & second digit.
first = int(two_digit_number[0])
second = int(two_digit_number[1])

#Make an addition of the 1st & 2nd digit.
print(first + second)
