from app import app, db
from flask import render_template, url_for, redirect
from app.models import Task
from app.forms import TaskForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        tasks = Task(title=form.title.data, status=False)
        db.session.add(tasks)
        db.session.commit()
    tasks = db.session.query(Task).all()
    
    return render_template('base.html', title='Home', tasks=tasks , form=form)

@app.get('/update/<int:task_id>')
def update(task_id):
    task = db.session.query(Task).filter(Task.id == task_id).first()
    #task = db.session.query(Task).filter(id=task_id).first()
    task.status = not task.status #dlaczego status nie  podświetla
    db.session.commit()
    return redirect(url_for("index", task=task))

@app.get('/delete/<int:task_id>')
def delete(task_id):
    task = db.session.query(Task).filter(Task.id == task_id).first()
    #task = db.session.query(Task).filter(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))