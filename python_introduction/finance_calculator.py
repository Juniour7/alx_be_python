# We are trying to calculate a user's monthly salary based on inputed monthly income and expenses.
# Prompt the user to input their monthly salary
# Prompt the user for thier monthly expenses
# Calculate mothly savings by subtracting expenses from the monthly salary
# Project annual savings assuming a simple annual interest rate of 5%
# Project savings after one year, incoporating the interest
# Display the user's monthly savings
# Display the projected annual savings after including the interest

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: ")) # Corrected typo: "mothly" to "monthly"

monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05

project_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Corrected print statements to match the example interaction's format and include '$' and two decimal places
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${project_annual_savings:.2f}.")