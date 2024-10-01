"""
1. The Range Riddle
Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

Task 1: Your Mood Today - Write a program that prints off different moods for each day of the week. 
Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm".
Using the range() function, loop through every day of the week and for each day randomly select a mood from the list and print it. 
Ensure that your program includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
"""
import random

moods = ["Happy", "Sad", "Entergetic", "Calm"]
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in (week_days):
    random_mood = random.choice(moods)
    print(f" On {day}, I was feeling {random_mood}")


"""
2. Double Scoop with Nested Loops
Objective: The aim of this assignment is to practice using nested loops in Python.

Task 1: Your Mood Tracker Simulator - a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"
"""
times_of_day = ["morning", "afternoon", "evening"]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
mood_types = ["Happy", "Sad", "Entergetic", "Calm", "Tired"]

for days in days_of_week:
    for time in times_of_day:
        random_moods = random.choice(mood_types)
        print(f"On {days} {time}, I was feeling {random_moods}")
