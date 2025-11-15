# daily_reminder.py

# Ask the user for a task
task = input("Enter your task: ")

# Ask for priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case to process priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify message if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print("\nReminder:", reminder)
else:
    reminder += ". Consider completing it when you have free time."
    print("\nNote:", reminder)
 
