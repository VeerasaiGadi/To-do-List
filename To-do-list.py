tasks = []

def add_task(task):
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

def remove_task(task):
  if task in tasks:
    tasks.remove(task)
    print(f"Task '{task}' removed from the list.")
  else:
    print(f"Task '{task}' not found in the list.")

def view_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("Your to-do list:")
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")

while True:
  choice = input("Choose an option:\n1. Add task\n2. Remove task\n3. View tasks\n4. Exit\n")

  if choice == "1":
    task = input("Enter the task: ")
    add_task(task)
  elif choice == "2":
    task = input("Enter the task to remove: ")
    remove_task(task)
  elif choice == "3":
    view_tasks()
  elif choice == "4":
    break
  else:
    print("Invalid choice. Please try again.")

