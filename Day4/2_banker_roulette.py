import random

# Split string method

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
print(names)

# Get total number of items in list

# num_items = len(names)
# print(num_items)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today.")


