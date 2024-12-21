"""
app.py

This file sets up a simple Flask ToDo application:
- Displays tasks on the home page.
- Allows adding new tasks.
- Allows deleting tasks.
- Allows toggling tasks as completed or not.
- Uses a Python list for storage (non-persistent).
"""

from flask import Flask, render_template, request, redirect, url_for

# Create a Flask instance (the WSGI application).
app = Flask(__name__)

# We'll store each task as a dictionary:
# { "description": <string>, "completed": <boolean> }
# For demonstration, let's start with two sample tasks.
tasks = [
    {"description": "Buy groceries", "completed": False},
    {"description": "Complete Python project", "completed": False},
]

@app.route('/')
def home():
    """
    The home route (index) serves the ToDo list page.
    It returns the 'home.html' template and passes the tasks list to it.
    """
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """
    Handles the form submission for adding a new task.
    'task_description' is fetched from the request form.
    If it's not empty, append a new dictionary to our tasks list
    with the 'description' and 'completed=False'.
    Then redirect to the homepage to show the updated list.
    """
    new_task_desc = request.form.get('task_description', '').strip()  # Get input and remove leading/trailing spaces
    if new_task_desc:
        # Append a dictionary representing the new task
        tasks.append({"description": new_task_desc, "completed": False})
    # Redirect back to the 'home' route
    return redirect(url_for('home'))

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    """
    Deletes a task at the specified 'task_index'.
    We check if the index is within range; if so, we remove it from the list.
    Then redirect back to display the updated list.
    """
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('home'))

@app.route('/toggle_complete/<int:task_index>', methods=['POST'])
def toggle_complete(task_index):
    """
    Toggles the 'completed' boolean flag of the task at 'task_index'.
    If it was True, set to False; if it was False, set to True.
    Then redirect to the homepage to show the updated status.
    """
    if 0 <= task_index < len(tasks):
        # Flip the 'completed' status
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    return redirect(url_for('home'))

# Entry point for running the Flask development server
if __name__ == '__main__':
    # debug=True reloads the server upon code changes (useful for development).
    app.run(debug=True)
