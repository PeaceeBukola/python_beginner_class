# # Exercise 8: The Smart ATM Challenge

# Hello Peace Alemede, my name is Jason from paystack, I am pleased to inform you that you have been hired as a Junior Python dev, your first task is to build us a basic ATM program, this is to test your ability to turn a real-world problem into a working Python solution.

# Your program must be organised into functions, use variables properly, perform calculations, and make decisions."

# 1. Create variables for a customer's name, PIN, and account balance
# 2. Create a function that accepts the customer's name and balance and returns a welcome message
# 3. Create a function that checks whether an entered PIN matches the correct PIN
# 4. Create a withdrawal function that accepts the balance and withdrawal amount
# 5. Reject incorrect PINs, zero or negative withdrawals, and withdrawals exceeding the balance
# 6. Calculate the new balance only when the transaction is valid
# 7. Return a clear transaction message and the updated balance

# ## Test cases

# | Scenario                                        | Expected behaviour        |
# | ----------------------------------------------- | ------------------------- |
# | Correct PIN, balance ₦10,000, withdrawal ₦3,000 | Success; balance ₦7,000   |
# | Incorrect PIN                                   | Reject transaction        |
# | Withdrawal of ₦15,000 from ₦10,000              | Reject; balance unchanged |
# | Withdrawal of ₦0                                | Reject invalid amount     |
# | Withdrawal of -₦500                             | Reject invalid amount     |
# | Withdrawal of ₦10,000 from ₦10,000              | Success; balance ₦0       |

# Bonus challenge: Allow the customer to choose between checking their balance, withdrawing money, and depositing money, you can use `if/elif/else` to handle the choices. 

# If your tutor have not taught lists or loops yet, you can simply call each function separately for now, those topics will be treated at the next standup meeting

# Important: This is a learning simulation, not a real banking security system
# A PIN stored directly in a Python variable is not secure for real banking





customers_name = 'Jason'
Pin = 1000
Balance = 10000

def customer_id (customers_name, Balance):
    return f"Welcome {customers_name}"

pin_pass = int(input("please input your pin: "))

def pin_match (Pin, pin_pass, Balance):
    if Pin == pin_pass :
        return "pin is correct"

    elif Pin != pin_pass:
        return "incorrect pin"

print((pin_match(Pin, pin_pass, Balance)))

withdrawal = int(input("how much would you like to withdraw?: "))
def withdraw_metric(withdrawal, Balance):
    new_balance = (Balance - withdrawal)
    if withdrawal <= 0:
        return "withdrawal rejected - invalid amount"
    elif withdrawal > Balance :
        return "withdrawal rejected - insufficient funds"
    elif withdrawal < Balance : 
        return f"Success; Balance = {new_balance}"    
    elif withdrawal == Balance:
        return f"All funds completely withdrawn - {new_balance}"


print(withdraw_metric(withdrawal, Balance))





#not fully inderstood also, and system thinking was not really done