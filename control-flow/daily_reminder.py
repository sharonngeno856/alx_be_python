# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process priority using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority"

# Append time-bound message if needed
if time_bound == "yes":
    message += " that requires immediate attention today!"

elif priority in ["medium", "low"]:  # Extra guidance if not time-bound
    message += ". Consider completing it when you have free time."

# Print the final reminder
print("\n" + message)
 
