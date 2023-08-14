# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# Try to use the exponent operator in your code.
# Remember to round your result to the nearest whole number.
# Make sure you include the words in bold from the interpretations.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

def print_bolt(text):
    print("\033[1m" + text + "\033[0m")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
rounded_bmi = round(bmi) 

if bmi < 18.5:
    print_bolt(f"Your BMI is {rounded_bmi}, you are underweight.")
elif 18.5 <= bmi <= 25:
    print_bolt(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif 25 < bmi <= 30:
    print_bolt(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif 30 < bmi <= 35:
    print_bolt(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print_bolt(f"Your BMI is {rounded_bmi}, you are clinically obese.")
