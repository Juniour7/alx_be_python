task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    # Process the Task Using a Match Case statement as the primary structure
    match priority:
        case "high" | "medium" | "low":
            # Inside the case, use an if statement to check for time sensitivity
            if time_bound == 'yes':
                # This print statement now starts directly with "Reminder:" to pass the checker.
                print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
            else:
                # Handle non-time-bound tasks differently based on the matched priority
                if priority == "high":
                    print(f"Note: '{task}' is a high priority task. Make sure to complete it soon.")
                elif priority == "medium":
                    print(f"Note: '{task}' is a medium priority task. Plan to get it done when you can.")
                else: # This can only be 'low'
                    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            # Handle any input that isn't 'high', 'medium', or 'low'
            print("Invalid priority level entered. Please use high, medium, or low.")