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


#Data type
#String
#int
#float
#bool
#list
#set

#arithmetic
#comparison/relational
#logical
#membership
#identity


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

# value1 = 6
# value2 = 8

x = 5
y = 2

# def add (value1, x): #input(parameters), output, operation, name
#     return value1 + x

# def subtract (x, value2):
#     return x - value2


# print(add(value1, x))
# print(subtract(x, value2))

# temp = int(input("Whats your body temperature?: "))

# def temp_checker(temp):
#     if temp <= 38:
#         return "You do not have fever"
#     else:
#         return "You have fever"

# print(temp_checker(temp))

# print(x / y) #floor division
# print(x // y) #floor division
# print(x % y) #modulus (remainder)
# print(x ** y) #raise to the power of

# #comparison/ relational operaitons
# print(x == y) #is equal
# print(x >= y) #is greater or equal
# print(x < y) #is less
# print(x != y) #is not equal

#logical operators: and, or, not
# logic       input       output
#and          T    T        T
            # T    F        F
            # F    T        F
            # F    F        F

#or           T    T        T
            # T    F        T
            # F    T        T
            # F    F        F

# age = int(input('How old are you: '))


# def age_checker(age):
#     if age >= 18 or age < 60:
#         return "you are eligible to vote"
#     else:
#        return "you are ineligible to vote"
# print(age_checker(age))



#membership: in, not in
numbers = ['a','b','c','d','e','f']
value = 5
if value in numbers:
    print('yes')
else:
    print('No')