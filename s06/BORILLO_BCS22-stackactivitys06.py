class Task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.completed = False


class TaskManager:
    def __init__(self, maxsize):
        self.tasklist = []
        self.maxsize = maxsize
        self.top = -1

    def isfull(self):
        return self.top == self.maxsize - 1

    def isempty(self):
        return self.top == - 1

    def addtask(self, title, desc):
        task = Task(title, desc)
        if not self.isfull():
            if task not in self.tasklist:
                self.top += 1
                self.tasklist.append(task)
                return f"Task '{title}' added successfully"
        else:
            return "Tasklist full. Please delete a task to add another."

    def deletetask(self, index):
        if not self.isempty():
            self.top -= 1
            self.tasklist.remove(self.tasklist[index])
            return f"Task #'{index + 1}' deleted successfully."
        else:
            return "Tasklist empty. Please add a task to delete."


    def taskcompleter(self, i):
        if 0 <= i < len(self.tasklist):
            if self.tasklist[i].completed == False:
                self.tasklist[i].completed = True
                return f"{self.tasklist[i].title} is complete."
            else:
                return "Task is already marked complete!"
        elif self.isempty():
            return ("Task list is empty.")
        else:
            return "Invalid input."

    def taskdisplay(self):
        if self.isempty():
            print("No tasks to display")
        else:
            print("Task List:")
            for i in range(len(self.tasklist)):
                status = "Completed!" if self.tasklist[i].completed is True else "Pending..."
                print(f"[{i + 1}]Title: {self.tasklist[i].title} | Description: {self.tasklist[i].desc} || ---> Status: {status}")

    def display(self):
        while True:
            print(f"""                                                        Task Manager                                
            ============================================================================================================
            ||                                                                                                        ||
            || [1]. Display all Tasks                                                                                 ||
            || [2]. Add a Task                                                                                        ||
            || [3]. Complete a Task                                                                                   ||
            || [4]. Delete a Task                                                                                     ||
            || [5]. Exit Task Manager                                                                                 ||
            ||                                                                                                        ||
            || Task List Size: {self.maxsize}                                                                                      ||
            ||                                                                                                        ||
            ============================================================================================================""")
            userin = input("""Choose an option! (Use the numbers ONLY)
>  """)

            if userin == "1":
                self.taskdisplay()

            elif userin == "2":
                title = input("\nEnter Task Title: ")
                description = input("Enter Task Description: ")
                print(self.addtask(title, description))

            elif userin == "3":

                print("Displaying current tasks: ")
                self.taskdisplay()
                if self.isempty():
                    print("Empty taskbar. Please add task to complete.")
                else:
                    com = int(input("\nEnter task number to mark as complete: "))
                    com = com - 1
                    print(self.taskcompleter(com))

            elif userin == "4":
                print("Displaying current tasks: ")
                self.taskdisplay()
                if self.isempty():
                    print("Empty taskbar. Please add task to delete.")
                else:
                    d = int(input("\nEnter task number to delete: "))
                    dlt = d - 1
                    print(self.deletetask(dlt))

            elif userin == "5":
                exit = input("\nExit? (Yes or No): ")
                if exit.lower() == "yes":
                    print("Exiting...")
                    break
                elif exit.lower() == "no":
                    continue
                else:
                    print("Invalid Option. Please enter 'Yes' or 'No'")

            else:
                print("Invalid.")
                print("Please select a valid option (1-5)")



maxin = int(input("""Enter Maximum Size:
>   """))
manager = TaskManager(maxin)
manager.display()
