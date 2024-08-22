to_do_list = []

while True:
    print("\nTo-Do List Manager")
    print("1. Add a Task")
    print("2. Mark Task as Done")
    print("3. Remove a Task")
    print("4. View Tasks")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':  
        task_name = input("Enter the task name: ")
        to_do_list.append([task_name, False])
        print(f"Task '{task_name}' added.")
    
    elif choice == '2':  
        if not to_do_list:
            print("No tasks to mark as done.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(to_do_list, 1):
                status = "Done" if task[1] else "Not Done"
                print(f"{i}. {task[0]} - {status}")
            try:
                task_num = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_num < len(to_do_list):
                    to_do_list[task_num][1] = True
                    print(f"Task '{to_do_list[task_num][0]}' marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == '3':  
        if not to_do_list:
            print("No tasks to remove.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(to_do_list, 1):
                status = "Done" if task[1] else "Not Done"
                print(f"{i}. {task[0]} - {status}")
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_num < len(to_do_list):
                    removed_task = to_do_list.pop(task_num)
                    print(f"Task '{removed_task[0]}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == '4':  
        if not to_do_list:
            print("No tasks in the list.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(to_do_list, 1):
                status = "Done" if task[1] else "Not Done"
                print(f"{i}. {task[0]} - {status}")
    
    elif choice == '5':  
        print("Exiting the To-Do List Manager.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
