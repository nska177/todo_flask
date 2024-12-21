Flask ToDo App
A beginner-friendly ToDo application built with Flask (Python) and styled using Bootstrap. This project demonstrates the basics of building a web app with Flask and deploying it for use.

Features
Add tasks: Create new tasks easily.
Mark tasks complete: Toggle a task’s status (completed or not).
Delete tasks: Remove tasks when no longer needed.
Responsive Design: Works on mobile, tablet, and desktop devices.
How to Set Up Locally
1. Prerequisites
Ensure you have the following installed:

Python (3.7 or higher)
Pip (Python package manager)
2. Clone the Repository
Download the code to your computer:

bash
Copy code
git clone https://github.com/your-username/flask-todo.git
cd flask-todo
3. Set Up the Environment
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
Install dependencies:

bash
Copy code
pip install flask
4. Run the App Locally
Start the Flask server:
bash
Copy code
python app.py
Open your browser and go to http://127.0.0.1:5000.
How to Deploy
Deploy on PythonAnywhere
Sign up for a free account on PythonAnywhere.
Create a new Web App:
Select Flask as the framework.
Choose the default Python version.
Upload your project files:
Use the PythonAnywhere file manager or SCP (secure copy) to upload app.py and the templates folder.
Edit the WSGI Configuration File:
Update the file to point to your app.py. Example:
python
Copy code
import sys
path = '/home/your-username/flask-todo'
if path not in sys.path:
    sys.path.append(path)
from app import app as application
Reload the web app. Your ToDo app is now live!
Next Steps
Use a database like SQLite to store tasks permanently.
Add more features like task priorities or due dates.
Explore more advanced Flask topics, such as user authentication.
