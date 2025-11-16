task = input("Enter your task:")
priority = input("Priority (high/medium/low)").lower()
time_bound = input("Is it time-bound? (yes/no)")

match priority:
    case "high":
        print(f"{task} is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"{task} is a medium priority task that requires attention later today!")
    case "low":
        print(f"{task} is a low priority task. Consider completing it when you have free time")