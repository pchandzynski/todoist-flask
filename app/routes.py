from app import app, db
from flask import render_template, url_for, redirect, flash, request
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

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    form = TaskForm()
    task = db.session.query(Task).filter(Task.id == task_id).first()

    if form.validate_on_submit():
        task.title = form.title.data
    #    task = Task(title=form.title.data)
    #    db.session.add(task)
        db.session.commit()
        return redirect(url_for("index"))
    
    # elif request.method == 'GET':
    #     form.title.data = task.title

    form.title.data = task.title
    return render_template('edit_task.html', form=form)

