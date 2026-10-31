# ## Exercise 7: The Personal Productivity Coach

# Scenario: Create a program that tells a student how to manage her day based on the number of hours she has available

# Your task:

# - Create a function that accepts the student's name, available hours, study hours, and sleep hours
# - Calculate how many hours remain for other activities
# - If study hours exceed available hours, return an error message
# - If sleep hours are less than 7, warn the student that she may not be getting enough sleep
# - If no hours remain after study and sleep, explain that her schedule is fully occupied
# - Otherwise, tell her how many free hours she has

# Example: Available = 24, study = 6, sleep = 8

# Expected result: 10 hours remain for other activities

# Think deeper:

# - What if the student enters negative study hours?
# - What if study hours plus sleep hours exceed 24?
# - How can you avoid repeating the same calculations in different places?

stud_name = "Theodore"
stud_av_hrs = 24
studyhrs = 10
sleephrs = 6


def stud_details(stud_name, stud_av_hrs, studyhrs, sleephrs):
    return (f"{stud_av_hrs - studyhrs - sleephrs} hours remain for other activities")

print(stud_details(stud_name, stud_av_hrs, studyhrs, sleephrs))

activityhrs = (studyhrs + sleephrs)
def productivity_metric(stud_av_hrs, studyhrs, sleephrs, activityhrs):
   
    if studyhrs > stud_av_hrs:
        return "error"

    elif studyhrs < 7: 
        return "you're not getting enough sleep"

    elif activityhrs >= stud_av_hrs:
        return "schedule fully occupied"

    elif stud_av_hrs > activityhrs:
        return f"{stud_av_hrs - activityhrs} remain"

print(productivity_metric(stud_av_hrs, studyhrs, sleephrs, activityhrs))





