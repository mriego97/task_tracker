# 🗂️ Task Tracker (Python CLI)

**Task Tracker** is a simple command-line interface (CLI) application written in Python that allows you to manage your daily tasks directly from the terminal. This application helps you track what you need to do, what you're currently working on, and what you've completed.

---

## 📌 Features

- ✅ Add new tasks with automatic creation date
- ✏️ Update task statuses (`not done`, `in progress`, `done`)
- ❌ Delete tasks by ID
- 📋 List all tasks or filter by their status
- 💾 Data persistence in a local `task.json` file

---

## 🧱 Task Structure

Each task is stored as a JSON object with the following properties:

| Property     | Type     | Description                                 |
|--------------|----------|---------------------------------------------|
| `id`         | Integer  | Unique identifier for the task              |
| `description`| String   | Short description of the task               |
| `status`     | String   | Task status: `not done`, `in progress`, `done` |
| `createdAt`  | String   | Date when the task was created              |
| `updatedAt`  | String   | Date when the task was last updated         |

---

## 🚀 How to Run
```bash
git clone https://github.com/mriego97/task-tracker.git
```
```bash
cd task-tracker
```

### 2. Run from the terminal

```bash
python task_tracker.py
```
### 📋 Menu Options

```text
1. Add New Task  
2. Delete Task  
3. Show All Tasks  
4. Filter Task by Status  
5. Change Task Status  
6. Exit
```

## 🧪 Example Usage
Add a task:

Introducing the name of the task: Read Python documentation
Change task status:


Enter the id of the task you want to change: 2  
Enter the status of the task you want to switch to: done
Filter tasks:
Introducing the status of the task you want to see (not done, in progress, done): in progress

## 📁 File Structure
graphql
task_tracker.py   # Main script file  
task.json         # Automatically created JSON file to store task data

## ⚠️ Constraints
Uses only the Python standard library (json, os, datetime)

Does not rely on external libraries or frameworks

Runs entirely in the command line

Handles user input errors and missing data gracefully

## 📚 Learning Objectives

This project helps reinforce:
📂 File handling with the filesystem
🧪 Input validation and error handling
🧾 JSON data manipulation
🖥️ Creating interactive CLI applications
🧱 Writing modular Python code
📝 License
This project is open-source and available under the MIT License.
