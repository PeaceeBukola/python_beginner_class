#create a function that checks age of a voter
#if age <= 18, return You are ineligible to vote
#else return You are eligible to vote



age = int(input('How old are you: '))

def age_checker(age):
    if age <= 18:
        return "you are ineligible to vote"
    else:
       return "you are eligible to vote"
print(age_checker(age))