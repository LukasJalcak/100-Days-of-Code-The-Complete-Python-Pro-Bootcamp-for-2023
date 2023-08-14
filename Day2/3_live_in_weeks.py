# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.

age = input("What is your current age? ")

new_age = 90 - int(age)
days = new_age * 365
weeks = new_age * 52
months = new_age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")