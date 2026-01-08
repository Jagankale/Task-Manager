"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High', 'deadline': '2026-01-10'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium', 'deadline': '2026-01-15'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low', 'deadline': '2026-01-20'},
]
@app.route('/')
def index():
    return render_template("index.html", tasks=TASKS)

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_task = {
            'id': len(TASKS) + 1,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority'],
            'deadline': request.form['deadline']
        }
        TASKS.append(new_task)
        return redirect(url_for("index"))

    return render_template("add.html")
@app.route("/task/<int:id>")
def task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/delete/<int:id>')
def delete(id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('index'))
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = next((t for t in TASKS if t['id'] == id), None)

    if task is None:
        return "Task not found", 404

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['status'] = request.form['status']
        task['priority'] = request.form['priority']
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
