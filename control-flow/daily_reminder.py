task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Process the Task Using a Match Case statement as the primary structure
    match priority:
        case "high" | "medium" | "low":
            # Inside the case, use an if statement to check for time sensitivity
            if time_bound == 'yes':
                # This single message format is used if the task is time-bound, regardless of priority.
                # It fulfills the requirement: "A message should be ‘that requires immediate attention today!’"
                # It also fulfills: "Print a reminder...that includes its priority level and whether immediate action is required"
                print(f"\nReminder: '{task}' is a {priority} priority task that requires immediate attention today!")
            else:
                # Handle non-time-bound tasks differently based on the matched priority
                if priority == "high":
                    print(f"\nNote: '{task}' is a high priority task. Make sure to complete it soon.")
                elif priority == "medium":
                    print(f"\nNote: '{task}' is a medium priority task. Plan to get it done when you can.")
                else: # This can only be 'low'
                    print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            # Handle any input that isn't 'high', 'medium', or 'low'
            print("\nInvalid priority level entered. Please use high, medium, or low.")