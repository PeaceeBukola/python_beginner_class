# ## Excercise 4: The School Result Analyzer

# Scenario: You are helping a lecturer create a program to grade medical students' examination scores

# Your task:

# - Create a function that accepts a student's name and score
# - Scores of 70–100 receive an A
# - Scores of 60–69 receive a B
# - Scores of 50–59 receive a C
# - Scores of 40–49 receive a D
# - Scores below 40 receive an F
# - Return a message containing the student's name, score, and grade
# - Reject scores below 0 or above 100 with an appropriate message

# Example: Name = Peace, score = 75.

# Expected result: `Peace scored 75 and received grade A.`

# Think deeper:

# - What happens when someone scores exactly 70?
# - Why does the order of your conditions matter?
# - What if the score is 105?

# Extra challenge: Add a second function that checks whether the student passed or failed




Name = any
Score = 64

def info(Name, Score):
    return (f"your name is {Name} you scored {Score}.")

print(info(Name, Score))


def grades(Name, Score):
        if Score >= 75 and Score <= 100 :
            return f"{Name} recieved {Score} and recieved an A grade"

        elif Score >= 60 and Score <= 69:
            return f"{Name} recieved {Score} and recieved a B grade"

        elif Score >= 50 and Score <= 59:
            return f"{Name} recieved {Score} and recieved a C grade"

        elif Score >=40 and Score <= 49:
            return f"{Name} recieved {Score} and recieved a D grade"

        elif Score <=39:
            return f"{Name} recieved {Score} and recieved an F grade"

        elif Score == 0 and Score > 100 :
            return "grade unapplicable"

print(grades(Name, Score))

            

            
            
            



