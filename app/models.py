from app import db


class Task(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(140))
    status = db.Column(db.Boolean)
    