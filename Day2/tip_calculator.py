print("Welcome to the tip calulator.")
total_bill = float(input("What was the total bill? "))
payers = int(input("how many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill_with_tip = (total_bill + (total_bill *  (tip/100))) / 5
#final_amount = round(total_bill_with_tip, 2)
final_amount ="{:.2f}".format(total_bill_with_tip)
print(f"Each person should pay {final_amount} $")