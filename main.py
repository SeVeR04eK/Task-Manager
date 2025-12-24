from time import sleep
from datetime import datetime
import shortuuid as su
import os


class Tasks:
    def __init__(self, idt, title, status, priority, data, description):
        self.idt = idt
        self.title = title
        self.status = status
        self.priority = priority
        self.data = data
        self.description = description

    def __str__(self): #info
        return (f"""id: {self.idt}
title: {self.title}
status: {self.status}
priority: {self.priority}
data: {self.data}
                
description: {self.description}""")


class Command:
    def __init__(self, comm_name, info):
        self.comm_name = comm_name
        self.info = info
        Command.all_comm_name.append(comm_name)

    all_comm_name =[]

    @classmethod
    def create(cls, tasksdef):
        title = input("Title of the task(required!): ")
        status = input("Status of the task(todo/in progress/done): ")
        priority = input("Priority of the task(low, medium, high): ")
        description = input("Description of the task(optional): ")
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        idt = "x" + su.random(length=8)
        tasksdef[idt] = Tasks(idt, title, status, priority, data, description)
        filename = idt + ".txt"
        try:
            with open("tasks/"+filename, "w") as f:
                f.write(tasksdef[idt].__str__())
            print("Tasks created successfully!")
        except FileNotFoundError:
            print("File not found")

    @classmethod
    def edit(cls, tasksdef):
        for i, com in enumerate(tasksdef.values(), start=1):
            print(f"{i}. {com.title}")
        answer = int(input("Choose task to edit: ")) - 1
        if answer + 1 > len(tasksdef) or answer + 1 < 1:
            print("Invalid choice")
        else:
            title = input("Title of the task(required!): ")
            status = input("Status of the task(todo/in progress/done): ")
            priority = input("Priority of the task(low, medium, high): ")
            description = input("Description of the task(optional): ")
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            listkey = [i for i in tasksdef.keys()]
            tasksdef[listkey[answer]] = Tasks(listkey[answer], title, status, priority, data, description)
            filename = listkey[answer] + ".txt"
            try:
                with open("tasks/" + filename, "w") as f:
                    f.write(tasksdef[listkey[answer]].__str__())
                print("Tasks edited successfully!")
            except FileNotFoundError:
                print("File not found")

    @classmethod
    def delete(cls, tasksdef):
        for i, com in enumerate(tasksdef.values(), start=1):
            print(f"{i}. {com.title}")
        answer = int(input("Choose task to edit: ")) - 1
        if answer + 1 > len(tasksdef) or answer + 1 < 1:
            print("Invalid choice")
        else:
            listkey = [i for i in tasksdef.keys()]
            filename = "tasks/" + listkey[answer] + ".txt"
            if os.path.exists(filename):
                os.remove(filename)  # удаляем
                print("Tasks deleted successfully!")
            else:
                print("Tasks not found.")
            del tasksdef[listkey[answer]]

    @classmethod
    def show(cls, tasksdef):
        for i, com in enumerate(tasksdef.values(), start=1):
            print(f"{i}. {com.title}")
        answer = int(input("Choose task to see: ")) - 1
        if answer + 1 > len(tasksdef) or answer + 1 < 1:
            print("Invalid choice")
        else:
            listkey = [i for i in tasksdef.keys()]
            filename = listkey[answer] + ".txt"
            try:
                with open("tasks/" + filename, "r") as f:
                    print("\n"+f.read())
            except FileNotFoundError:
                print("File not found")


    @classmethod
    def command(cls, tasksdef):
        for i, com in enumerate(cls.all_comm_name, start=1):
            print(f"{i}. {com}")
        sleep(1.5)
        print("\nChoose option(1-4): ")
        answer = int(input())
        if answer == 1:
            cls.create(tasksdef)
        elif answer == 2:
            cls.edit(tasksdef)
        elif answer == 3:
            cls.delete(tasksdef)
        elif answer == 4:
            cls.show(tasksdef)
        else:
            print("Invalid input.")


#Front
create_task = Command('Create task', "")
edit_task = Command('Edit task', "")
delete_task = Command('Delete task', "")
show_task = Command('Show task-list', "")

def load_tasks_from_files(folder="tasks"):
    tasksdef = {}
    if not os.path.exists(folder):
        os.makedirs(folder)  # если папки нет — создаём
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                idt = f.readline().strip().replace("id: ", "")
                title = f.readline().strip().replace("title: ", "")
                status = f.readline().strip().replace("status: ", "")
                priority = f.readline().strip().replace("priority: ", "")
                data = f.readline().strip().replace("data: ", "")
                f.readline()  # пропускаем пустую строку
                description = f.readline().strip().replace("description: ", "")
                tasksdef[idt] = Tasks(idt, title, status, priority, data, description)
        except FileNotFoundError:
            print("File not found")
    return tasksdef

def intro():
    print("HI!".center(50, "-"))
    sleep(2)
    print("Welcome to Task Manager!".center(50, "-"))
    sleep(3)
    print("My name is Andrii".center(50, "-"))
    sleep(2)
    print("And it's my first ever project".center(50, "-"))
    sleep(3)
    print("Have fun!".center(50, "-"))
    print("")
    sleep(3)

def main():
    Command.command(tasks)

tasks = load_tasks_from_files()
intro()

while True:
    print()
    main()