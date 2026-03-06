import os
import json
import uuid 

# for v2 could separete the pending and completed task file

# create todo.json if dosen't exists
if not os.path.exists("todo_completed.json"):
    with open("todo_completed.json", "w") as f:
        json.dump([], f)

if not os.path.exists("todo_pending.json"):
    with open("todo_pending.json", "w") as f:
        json.dump([], f)


file_path_pending = os.path.join(os.getcwd(), "todo_pending.json")
file_path_completed = os.path.join(os.getcwd(), "todo_completed.json")


def task_add(file_path: str)-> str:
    """
    This function adds a task to the todo list.

    It takes a file path as argument and uses it to read and write the todo list.
    The function asks the user for the task to be added and generates a unique id for it.
    It adds the task to the list and writes it back to the file.

    Returns a string with a success message.
    """
    input_data = input("Task: ")
    id = str(uuid.uuid4())

    data = {
        "id": id,
        "task": input_data,
        "status": "pending"
    }

    with open(file_path, "r") as f:
        old_data = json.load(f)

    old_data.append(data)

    with open(file_path, "w") as f:
        json.dump(old_data, f)


    return "\nTask added successfully\n"



def task_view(file_path_pending: str, file_path_completed: str)-> None:
    """
    This function views the tasks in the todo list.

    It takes a file path as argument and uses it to read the todo list.
    The function separates the tasks into pending and completed tasks and prints them out.
    If there are no pending or completed tasks, it prints a relevant message.
    """
    with open(file_path_pending, "r") as f:
        pending_data = json.load(f)
    # print(pending_data)
    
    with open(file_path_completed, "r") as f:
        completed_data = json.load(f)
    # print(completed_data)


    print("\033[92mPending Tasks\033[1m\n")

    if not pending_data:
        print("Add tasks")
    else:
        for index, item in enumerate(pending_data):
            print(f"{index+1}. {item['task']}")
        
    print("\n\033[92mCompleted Tasks\033[1m\n")
    if not completed_data:
        print("No completed task\n")
    else:
        for index, item in enumerate(completed_data):
            print(f"{index+1}. {item['task']}")
    print()



def task_done(file_path_pending: str, file_path_completed: str)-> str:

    with open(file_path_pending, "r") as f:
        pending_data = json.load(f)
    
    with open(file_path_completed, "r") as f:
        completed_data = json.load(f)
    
    try:
        to_update = int(input("Enter task number: ")) - 1
    except ValueError:
        return "Invalid input"

    if to_update >= 0 and to_update < len(pending_data):
        pending_data[to_update]["status"] = "completed"

        completed_data.append(pending_data[to_update])
        pending_data.remove(pending_data[to_update])

        with open(file_path_pending, "w") as f:
            json.dump(pending_data, f)

        with open(file_path_completed, "w") as f:
            json.dump(completed_data, f)
    else:
        return "Task not found" 

def task_delete(file_path: str)-> str:
    with open(file_path, "r") as f:
        data = json.load(f)

    try:
        to_delete = int(input("Enter task number: ")) - 1
    except ValueError:
        return "Invalid input"
    
    if to_delete >= 0 and to_delete < len(data):
        data.remove(data[to_delete])

        with open(file_path, "w") as f:
            json.dump(data, f)

    else:
        return "Task not found"

    
# task_add(file_path=file_path_pending)
# task_view(file_path_pending=file_path_pending, file_path_completed=file_path_completed )
# print("done ", task_done(file_path_pending=file_path_pending, file_path_completed=file_path_completed))
# print("delete ", task_delete(file_path_pending=file_path_pending))


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;37mMy Todo List\033[0m\n")
    print("-"*30, "\033[1m")
    task_view(file_path_pending=file_path_pending, file_path_completed=file_path_completed)

    print("\nSelect an option:\n")
    print("1. Add task\n2. Mark task as done\n3. Delete pending task\n4. Delete completed task\n5. Quit\n")

    try:
        option = int(input("Enter option: "))
    except ValueError:
        continue 

    if option == 1:
        task_add(file_path=file_path_pending)
    elif option == 2:
        task_done(file_path_pending=file_path_pending, file_path_completed=file_path_completed)
    elif option == 3:
        task_delete(file_path=file_path_pending)
    elif option == 4:
        task_delete(file_path=file_path_completed)
    elif option == 5:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    
        

print("\033[0m")