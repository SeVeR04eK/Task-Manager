from time import sleep
from tasks import load_tasks_from_files
from storage import Command

#Front
create_task = Command('Create task', "")
edit_task = Command('Edit task', "")
delete_task = Command('Delete task', "")
show_task = Command('Show task-list', "")

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
    main()