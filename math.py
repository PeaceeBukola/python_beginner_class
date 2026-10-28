#create a function that takes price of 2 items and add it together, let item1 =500, item2 = 700

# item1 = 500
# item2 = 700

# def add(item1, item2):
#     return item1 + item2

# print(add(item1, item2))

budget = 5000
shirt = 4000
shoes = 1500
transport = 500


def expenses(budget, shirt, shoes, transport):
    return budget - shirt - shoes - transport

def shopping_funds():
    total_spent = (shirt + shoes + transport)
    if expenses > budget:
        return budget - total_spent; extra-needed

    elif expenses == budget:
        return "you have nothing left"

print(shopping_funds())
