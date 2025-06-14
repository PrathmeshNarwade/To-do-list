def to_do_list():
    tasks = []
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Save as file")
        print("5. Quit")
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("Invalid input!, Please Enter a Number.")
            continue
        if choice == 1:
            task = input("Enter Task: ")
            tasks.append(task)
        elif choice == 2:
            task = input("Enter Task: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not Found!")

        elif choice == 3: 
            print("tasks: ")
            for task in tasks:
                print("- " + task)
        elif choice == 4:
            with open("to-do-list.txt", "w") as p:
                for task in tasks:
                    p.write(task + "\n")
        elif choice == 5:
            break
                
        else:
            print("Invalid choice")
to_do_list()
