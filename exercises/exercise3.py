# ## Excercise 3: Build a Mini Restaurant Billing System

# Scenario: A small restaurant needs a simple program to calculate a customer's bill

# Menu prices:

# - Rice: ₦2,000
# - Chicken: ₦1,500
# - Drink: ₦500

# Your task:

# 1. Create a function that accepts the quantity of rice, chicken, and drinks
# 2. Calculate the total bill using the menu prices
# 3. Accept the customer's payment amount as another parameter
# 4. If the payment is greater than the bill, calculate the change
# 5. If the payment equals the bill, print `"Payment successful!"`
# 6. If the payment is less than the bill, calculate how much the customer still owes

# Example test: 2 rice, 1 chicken, 2 drinks, payment of ₦7,000.

# Expected calculation: Total = ₦6,500; change = ₦500

# Think deeper: What if the customer orders zero drinks? Should the program still work?



rice = 2000
chicken = 1500
drink = 500

def menu(rice, chicken, drink):
    return rice*2 + chicken + drink*2

print(menu(rice, chicken, drink))

customer_px = int(input("amout_paid: "))

def payment(customer_px):
    menu_total = (rice*2 + chicken + drink*2)
    change = customer_px - menu_total
    if customer_px > menu_total:
        return change, "change left"

    elif customer_px == menu_total:
        return "payment successful"

    elif customer_px < menu_total:
        return  abs(change), "is left to blnce"
    
print(payment(customer_px))