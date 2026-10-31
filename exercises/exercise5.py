# ## Exercise 5: The Mini Banking Assistant

# Scenario: You are building a simple banking assistant that helps a customer withdraw money

# Your task:

# - Create a function that accepts the account balance and withdrawal amount
# - If the withdrawal amount is zero or negative, return an invalid amount message
# - If the withdrawal amount is greater than the balance, reject the transaction
# - Otherwise, subtract the withdrawal amount from the balance
# - Return the updated balance and a transaction message

# Example: Balance = ₦20,000; withdrawal = ₦7,500

# Expected result: New balance = ₦12,500

# Think deeper:

# - What happens when the withdrawal equals the balance?
# - Should a customer be allowed to withdraw ₦0?
# - Why should the original balance not be reduced when a transaction is rejected?

# Extra challenge: Write another function that accepts a deposit amount and returns the new balance


balance = 10000
withdrawal = 7500


def statement(balance, withdrawal):
    return f"Balance = {balance}, Withdrawal = {withdrawal} "

def new_balance(balance, withdrawal): 
    new_statement = int(balance - withdrawal) 
    if withdrawal <= 0 :
        return "invalid amount"

    elif withdrawal > balance :
        return ("transaction rejected - insufficient funds")

    elif withdrawal < balance:
        return new_statement, "remaining in account"

print(new_balance(balance, withdrawal))


deposit = int(input("how much was deposited: "))


def deposited_balance(balance, deposit):
    new_total = deposit + balance
    return "your total funds is", new_total
print(deposited_balance(balance, deposit))