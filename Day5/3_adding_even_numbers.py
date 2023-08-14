# Return the sum of the odd numbers from 1 to 100

# 1_solution
sum_of_odd_numbers = 0
for number in range(1, 101, 2):
    sum_of_odd_numbers += number
print(sum_of_odd_numbers)
# 2_solution
sum_of_odd_numbers = 0
for number in range(1, 101):
    if number % 2 > 0:
        sum_of_odd_numbers += number
print(sum_of_odd_numbers)

# Return the sum of the even numbers from 1 to 100

# 1_solution
sum_of_even_numbers = 0
for number in range(2, 101, 2):
    sum_of_even_numbers += number
print(sum_of_even_numbers)
# 2_solution
sum_of_even_numbers = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_of_even_numbers += number
print(sum_of_even_numbers)