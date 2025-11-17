
Task = input("Enter your task:")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()


match Priority:
    case "high":
        reminder = f"Your task '{Task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{Task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{Task}' is LOW priority."
    case _:
        Reminder = f"Your task '{Task}' has an UNKNOWN priority."
        

if Time_bound == "yes":
    Reminder += " That requires immediate attention today!"


print("\nToday's Reminder:")
for i in range(1):  
    print(Reminder)
