# ## Excercise 2: The Mystery Number Detective

# Scenario: A game gives a player a secret number, The program must analyse the number and reveal its properties

# Your task:

# - Create a function that accepts a number
# - If the number is greater than 100, return `"Big number!"`
# - If it is less than 100, return `"Small number!"`
# - If it is exactly 100, return `"You found the target!"`

# Test values: 50, 100, and 150.

# Think deeper:

# - What happens when the number is zero?
# - What happens when the number is negative?
# - Can your function return both a message and the calculated results?

# Rule: You must use a function and `if/elif/else`, not write three separate programs



secret_no = int(input("what is your number: " ))

def no_detector(secret_no):
    if secret_no > 100:
        print ("Big number")

    elif secret_no < 100 and secret_no > 0:
        print ("small number") 

    elif secret_no == 100:
        print ("You found the target!")

    elif secret_no < 0:
        print ("oops, you've hit a negative wall")

print (no_detector(secret_no))