# Personal Daily Reminder

#Ask the user for a task , Ask for priority, Ask if time-bound
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    
    #process using matchcase 
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task} is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority level"
     
    # Modify message if task is time-bound       
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    elif time_bound == "no":
        message += ". Consider completing it when you have free time."
   
   # Print the final message
    print("\nReminder: ", message)
    
    break