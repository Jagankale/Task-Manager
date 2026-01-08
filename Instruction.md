# Part 6: Homework - Personal To-Do List App

Build a Flask-based To-Do List application using everything you learned in Parts 1-5.

---

## Requirements

### 1. Create 4 Routes

| Route | Description |
|-------|-------------|
| `/` | Home page - display all tasks |
| `/add` | Page with a form to add new task |
| `/task/<int:id>` | View single task details |
| `/about` | About the app page |

### 2. Create Templates Folder

Create these HTML files inside `templates/` folder:

```
templates/
├── base.html      <- Base template (use template inheritance)
├── index.html     <- List all tasks
├── add.html       <- Form to add task
├── task.html      <- Single task detail
└── about.html     <- About page
```

### 3. Data Structure

Use this sample data in your `app.py`:

```python
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]
```

> **Note:** Data is stored in a Python list (in-memory). All tasks will reset when the server restarts. No database is used in this basic exercise.

### 4. Jinja2 Features to Use

Practice these Jinja2 features in your templates:

| Feature | Example |
|---------|---------|
| Variables | `{{ task.title }}` |
| Loops | `{% for task in tasks %}` |
| Conditionals | `{% if task.status == 'Completed' %}` |
| Filters | `{{ task.title\|upper }}` |

---

## Folder Structure

```
part-6/
├── app.py
├── Instruction.md
└── templates/
    ├── base.html
    ├── index.html
    ├── add.html
    ├── task.html
    └── about.html
```

---

## Step-by-Step Guide

1. **Start with app.py** - Create your Flask app and define the TASKS list
2. **Create base.html** - This is your master template with `{% block content %}{% endblock %}`
3. **Create index.html** - Extend base.html, loop through tasks and display them
4. **Create task.html** - Show details of a single task using `task.id`
5. **Create add.html** - Create a simple form (styling is optional)
6. **Create about.html** - Write a short description about your app

---

## Bonus Challenges (Optional)

- Add a `/priority/<name>` route to filter tasks by priority (High/Medium/Low)
- Add due dates to tasks and display them
- Create a dashboard showing task statistics (total tasks, completed count, etc.)

---

## How to Run

```bash
# Make sure venv is activated
python app.py
# Open browser: http://localhost:5000
```

Good luck!
