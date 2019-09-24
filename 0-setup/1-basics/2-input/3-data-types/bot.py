#BMI program
print("What is your name human?")
name = input()
print(name) #Added whilst testing to ensure variable is correct
print("\nHow old are you (in years)?")
age = int(input())
print(age) #Added whilst testing to ensure variable is correct
print("\nHow tall are you (in meters)?")
height = float(input())
print(height) #Added whilst testing to ensure variable is correct
print("\nHow much do you weight (in kilograms)?")
weight = float(input())
print(weight) #Added whilst testing to ensure variable is correct
height_squared = (height*height)
print(height_squared) #Added whilst testing to ensure variable is correct
bmi = (weight/height_squared)
print(name," you are ",age, "years old and your bmi is ",bmi)