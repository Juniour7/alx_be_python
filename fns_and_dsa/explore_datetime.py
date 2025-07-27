from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a specific format.
    """
    # Obtain the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates a future date.
    """
    try:
        # Prompt the user to enter a number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date
        current_date = datetime.now()
        
        # Calculate the future date by adding the specified number of days
        future_date = current_date + timedelta(days=number_of_days)
        
        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    """Main function to run the datetime exploration script."""
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()