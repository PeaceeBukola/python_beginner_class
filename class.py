# #Programming, Variable, VAlue, Algorithm, 
# firstname          =                'Peace'
# lastname           =                "Alemede"
# print(f"My name is {firstname}  {lastname}")
# print("{firstname} {lastname}")
#function
# name = "Peace"
# age = 24
# location = "Abuja"

# def welcome(name, age, location):
#     return f"How are you {name}, you are {age} years old and you are located in {location}"



# print(welcome(name, age, location))

    
# #Arithmethic operators
# x = 2
# y = 5

# add  = x + y
# subtract = x - y
# mult  = x * y
# print(add)
# print(subtract)
# print(mult)

value1 = 6
value2 = 8

x = 67
y = 13

temp = 40

def add (value1, x): #input(parameters), output, operation, name
    return value1 + x

def subtract (x, value2):
    return x - value2


print(add(value1, x))
print(subtract(x, value2))


if temp <= 38:
    print ("You dont have fever")
else:
    print("You have a fever")