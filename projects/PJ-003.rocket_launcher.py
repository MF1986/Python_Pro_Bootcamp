print('''
***********************************************************************
                                  88                                     
                                  88                    ,d               
                                  88                    88               
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8  ,adPPYba, MM88MMM ,adPPYba,  
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"  a8P_____88   88    I8[    ""  
88         8b       d8 8b         8888[    8PP"""""""   88     `"Y8ba,   
88         "8a,   ,a8" "8a,   ,aa 88`"Yba, "8b,   ,aa   88,   aa    ]8I  
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a `"Ybbd8"'   "Y888 `"YbbdP"' 


***********************************************************************
''')

print()
print("welcome on the launch pad!")
print("Your mission is to lauch the rocket.")
print()
print()

Q1 = input("Do you want to launch the rocket now? Yes or No? ").lower()
if Q1 == "no" :
  Q2 = input("We have a small booster for 8 crew members and a satelitte, is it enough? Yes or No ").lower()
  if Q2 == "no" :
    Q3 = input("At wich speed our Space Shuttle is traveling per meter second? 900, 1100, 1300 m/s? ").lower()
    if Q3 == "1300" :
      print("your rocket is now orbiting the earth! Congratulations!")
    else:
      print("your rocket is not going fast enough, it will fall back to earth!")
  else:
    print("You rocket doesn't have enough power to lift off, you loose!")
else:
  print("Unfortunately, you loose! There is no fuel to launch your rocket!")
