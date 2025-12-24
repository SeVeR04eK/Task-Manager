# Lightweight CLI Task Manager
A simple command-line task manager written in Python. Tasks are stored as text files inside the `tasks/` directory.

## Features
- Create tasks
- Edit tasks
- Delete tasks
- View task details
- Automatically generated unique task IDs
- Tasks are loaded automatically on startup

## Installation
Clone the repository and create a virtual environment:

```bash
git clone https://github.com/SeVeR04eK/Task-Manager.git
cd Task-Manager
python -m venv .venv
```

### Activate the environment:

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Usage
The program displays a menu with four options:
1. Create task
2. Edit task
3. Delete task
4. Show task

Each option guides you through the required input.

## Project Structure
```
Task-Manager/
├── tasks/                 # Stored task files
├── main.py                # Entry point
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements
- Python 3.12+
- shortuuid

## License
MIT License