import random
list = ["Heads", "Tails"]

len_list = len(list)
random_throw = random.randint(0, len_list - 1)
throw = list[random_throw]
print(throw)
# if random_throw == 1:
#     print("Heads")
# else:
#     print("Tails")