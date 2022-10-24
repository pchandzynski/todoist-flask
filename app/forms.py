from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, SubmitField


class TaskForm(FlaskForm):
    title = TextAreaField('What is your task?',  validators=[DataRequired()])
    add_task = SubmitField('Add task')

# class EditTaskForm(FlaskForm):
#     title = TextAreaField('Edit Your task', validators=[DataRequired()])
#     edit_task = SubmitField('Edit Task')