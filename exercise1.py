## Excercise 1: Warm up

# Scenario: I have ₦5,000 and want to go shopping, i need to know if i can afford everything i want to buy

# Help me:

# - Create variables for my budget, the price of a shirt, shoes, and transport
# - Create a function that accepts the budget and all three expenses
# - Calculate the total expenses
# - Return the money remaining
# - If i spend more than my budget, tell me how much extra i need
# - If i spend exactly my budget, tell me i have nothing left

# Test values:

# - Budget: ₦5,000
# - Shirt: ₦2,000
# - Shoes: ₦1,500
# - Transport: ₦500

# Expected result: I have ₦1,000 remaining

# Think deeper: What should happen if the Shirt costs ₦4,000 instead?


# budget = 5000
# shirt = 2000
# shoes = 1500
# transport = 500

# def expenses(budget, shirt, shoes, transport):
#     return (budget - (shirt + shoes + transport))


# def shopping_funds():
#     total_spent = (shirt + shoes + transport)

#     remaining = budget - total_spent
#     if remaining > 0 :
#         return remaining, "naira spare"
#     else:
#         return remaining, "extra needed"

# print (shopping_funds())


budget = 5000
shirt = 4000
shoes = 1500
transport = 500

def shopping_funds():
    total_spent = (shirt + shoes + transport)

    remaining = budget - total_spent
    if remaining > 0 :
        return remaining, "naira spare"
    else:
        return abs(remaining), "extra needed"

print (shopping_funds())