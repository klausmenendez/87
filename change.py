print("Please enter an amount less than a dollar")
value = int(input())
quarters = value//25
dimes = (value % 25)//10
nickels = ((value % 25) % 10)//5
pennies = (((value % 25) % 10) % 5)
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N", nickels)
print("P", pennies)