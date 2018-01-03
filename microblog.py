#set FLASK_APP=microblog.py (run this in cmd before running the script, it sets a needed environment variable.
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User':User, 'Post':Post}
#use "flask run" in cmd to run this, not python microblog.py