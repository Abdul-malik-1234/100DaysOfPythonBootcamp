print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or  N: ")

total_bill=0

#adding to bill for size
if size=='S':
    total_bill+=15
elif size=='M':
    total_bill+=20
else:
    total_bill+=25
#adding to bill for pepperoni
if pepperoni=='Y':
    if size=='S':
        total_bill+=2
    else:
        total_bill+=3
#adding to bill for extra cheese
if extra_cheese=='Y':
        total_bill+=1

print("Your final bill is: $"+str(total_bill)+".")
print("Thanks for ordering pizza from us.")
print("Have a great day.")