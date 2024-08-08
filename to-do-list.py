def menu():
    print("\nTo Do Menu")
    print("1. add task on list")
    print("2. view task on list")
    print("3. remove task on list")
    print("4. Exit")

def add_task(task):
    tasks =input("Enter your task:")
    task.append(tasks)
    print("Task added.")


def view_task(task):
    if not task:
        print("No task you added.")
    else:
        for i, tasks in enumerate(task,1):
            print(f"{i}. {tasks}.")


def delete_task(task):
    if not task:
        print("No task available to delete.")
    
    view_task(task)

    try:
        task_number = int(input("Enter your task number to be deleted: "))
        if 1 <= task_number <= len(task):
            remove_task = task.pop(task_number - 1)
            print(f"Task '{remove_task}' deleted.")
        else:
            print("invalid task number")
    except ValueError:
        print("Invalid input.Please enter a number")


def main():
    task=[]
    while True:
        menu()
        opt = int(input("Choose an option: "))
        if opt == 1:
            add_task(task)
        elif opt == 2:
            view_task(task)
        elif opt == 3:
            delete_task(task)
        elif opt == 4:
            print("App is exit. Good Bye!")
            break
        else:
            print("Invalid choice. Please select above only.")


main()