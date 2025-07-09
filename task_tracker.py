
from datetime import datetime
import json
import os

TASK_FILE = "task.json"

# Cargar Tareas
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

# Guardar Tareas
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Buscar next id
def get_next_id(tasks): 
    return max([task['id'] for task in tasks], default=0) + 1

def search_index(task_id):
    tasks = load_tasks()
    no_encontrado = True
    i=0
    try:
        while no_encontrado : 
            if task_id == tasks[i]['id']:
                no_encontrado = False
            else:
                i +=1
    except IndexError:
        # Posicion no encontrada
        return -1
    # Posicion
    return i
    
# Añadir Tareas
def add_task(description):
    date_today =  datetime.now().strftime("%d/%m/%Y")
    tasks = load_tasks()
    new_task = {"id": get_next_id(tasks),"description": description, "status": "not done", "createdAt": date_today, "updatedAt":"" }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# Eliminar Tareas
def delete_task(task_id):
    tasks = load_tasks()
    index = search_index(task_id)
    if index>=0:
        print(f"The tasks {tasks[index]['description']} has been deleted")
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print(f"The task was not found")
    
# Mostrar tareas
def show_task():
   tasks = load_tasks()
   print(tasks[0]['id'])
   for task in tasks:
       print(f"{task.get('id')}.Descripcion:{task.get('description')}.\nEstado:{task.get('status')}.\nFecha de creacion:{task.get('createdAt')}.\nFecha de modificacion:{task.get('updatedAt')}")
       print(f"**************************")
    
# Mostrar tareas por estado
def show_status_task(status):
    if status not in ["not done", "in progress", "done"]:
        print (f"Invalid status")
    else: 
        tasks = load_tasks()
        filted_task =  [t for t in tasks if t["status"] == status]
        for task in filted_task:
            print(f"{task.get('id')}.Descripcion:{task.get('description')}.\nEstado:{task.get('status')}.\nFecha de creacion:{task.get('createdAt')}.\nFecha de modificacion:{task.get('updatedAt')}")
            print(f"**************************")

# Modifica estado de la tarea
def mark_status_task(task_id, status):
    if status not in ["not done", "in progress", "done"]:
        print (f"Invalid status") 
    else:
        date_today =  datetime.now().strftime("%d/%m/%Y")
        tasks = load_tasks()
        indice = search_index(task_id)
        tasks[indice]['status'] = status
        tasks[indice]['updatedAt'] = date_today 
        save_tasks(tasks)
        print(f"Updated")


def main():
    while True:
        print(f"**********************************")
        print(f"---- WELCOME TO TASK TRACKER ---- ")
        print(f"**********************************")
        print(f"Choose the option (1-6)")
        print(f"1. Add New Task")
        print(f"2. Delete Task")
        print(f"3. Show All Tasks")
        print(f"4. Filter Task by Status")
        print(f"5. Change Task Status")
        print(f"6. Salir")
        print(f"")
        print(f"")
        try:
            option = input("Enter an Option (1-6): ")
            print(option)
        except ValueError:
            print("Please enter a valid number between 1 and 6.")
            continue

        if option == '1':
            add_task(input("Introducing the name of the task: "))
        elif option == '2':
            print(f"**********************************")
            show_task()
            delete_task(int(input("Introducing the number of the task: ")))
        elif option =='3':
            show_task()
        elif option == '4':
             show_status_task(input("Introducing the status of the task you want to see (not done, in progress, done): "))
        elif option == '5':
            id = int (input("Enter the id of the task you want to change: "))
            status= input("Enter the status of the task you want to switch to: ")
            mark_status_task(id, status)
        elif option == '6':
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")
            
        print("\n--- Press Enter to continue ---")
        input()
if __name__ == "__main__":
    main()