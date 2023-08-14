import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

test_h = float(input("Height of wall: "))
test_w = float(input("Width of wall: "))
coverage = float(input("Coverage per can: ")) 
paint_calc(height=test_h, width=test_w, cover=coverage)