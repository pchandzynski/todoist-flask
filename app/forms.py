from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import TextAreaField, SubmitField


class TaskForm(FlaskForm):
    title = TextAreaField('What is your task?',  validators=[DataRequired()])
    add_task = SubmitField('Add task')

