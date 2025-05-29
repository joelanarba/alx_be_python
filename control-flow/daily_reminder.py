# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case to process priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Append time sensitivity info
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print final reminder
print("\n" + message)