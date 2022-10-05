from app import app, db
from flask import render_template
from app.models import Task
from app.forms import TaskForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        tasks = Task(title=form.title.data)
        db.session.add(tasks)
        db.session.commit()
    tasks = db.session.query(Task).all()
    return render_template('base.html', title='Home', tasks=tasks , form=form)