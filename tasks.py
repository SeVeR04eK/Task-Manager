import os

class Tasks:
    def __init__(self, idt, title, status, priority, data, description):
        self.idt = idt
        self.title = title
        self.status = status
        self.priority = priority
        self.data = data
        self.description = description

    def __str__(self):  # info
        return (f"""id: {self.idt}
title: {self.title}
status: {self.status}
priority: {self.priority}
data: {self.data}

description: {self.description}""")

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