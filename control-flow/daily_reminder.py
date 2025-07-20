task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else :
            print(f"\nNote: '{task}' is a high priority task. Make sure to complete it soon.")
    case "medium":
        if time_bound.lower() == 'yes':
            print(f"\nReminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Plan to get it done today.")
    case "low":
            if time_bound.lower() == 'yes':
                print(f"\nReminder: '{task}' is a low priority task, but it requires immediate attention today!")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
        
    case _:
            print("\nInvalid priority level entered. Please run the script again and choose from high, medium, or low.")