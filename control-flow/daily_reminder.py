
Task = input("Enter your task:")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
    case "high":
        print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"Reminder: {Task} is a medium priority task that requires immediate attention later today!")
    case "low":
        print(f'Note {Task} is a low priority task. Consider completing it when you have free time')