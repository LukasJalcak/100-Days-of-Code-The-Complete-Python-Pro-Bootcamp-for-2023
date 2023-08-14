# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
first_digit_number = two_digit_number [0]
second_digit_number = two_digit_number [1]
result = int(first_digit_number) + int(second_digit_number)
print(result)