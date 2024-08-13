print('Welcome to the tip calculator!')
print('What was the total bill? ', end="$")
bill = float(input())
print('How much tip would you like to give? 10,12, or 15?', end=" ")
tip = int(input())
print('How many people to split the bill?', end="")
people = int(input())
individualBill = (bill+bill*(tip/100))/7
print(f"Each person should pay: ${round((bill+bill*(tip/100))/7,2)}")
