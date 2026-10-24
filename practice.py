#create a function that takes a budget, price1, price2, let the function add the two prices and remove it from the budget and prints the remaining, 
#let the budget be 1000. Let price1 = 200 and price2 = 700.
#Expected output is 100

budget = 1000
price1 = 200
price2 = 700

def remaining_funds(budget, price1, price2):
    return int(budget - (price1 + price2))

print(remaining_funds(budget,price1,price2))