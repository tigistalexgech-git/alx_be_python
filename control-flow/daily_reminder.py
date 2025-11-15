# Personal Daily Reminder

#Ask the user for a task , Ask for priority, Ask if time-bound
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    
    #process using matchcase 
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task} is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority level"
     
    # Modify message if task is time-bound       
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
   
   # Print the final message
    print("\nReminder: ", reminder)
    
    break