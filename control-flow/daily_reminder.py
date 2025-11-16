# daily_reminder.py

# Ask the user for task details
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is LOW priority."
    case _:
        reminder = f"Your task '{task}' has an UNKNOWN priority."
        
# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Print reminder (loop used to emphasize the message)
print("\nToday's Reminder:")
for i in range(1):   # simple loop (runs once to meet requirement)
    print(reminder)
