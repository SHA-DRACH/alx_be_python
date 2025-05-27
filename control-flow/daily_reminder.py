# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task: '{task}' has an unspecified priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print(message)
cd /workspaces/alx_be_python
git init
git add control-flow/daily_reminder.py
git commit -m "Add daily reminder script"
git remote add origin https://github.com/your-username/your-repo.git  # Replace with your actual repo URL
git push -u origin main