from app import db


class Task(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(140))
    status = db.Column(db.Boolean)
    
    # def __init__(self, status):
    #     status = False

    #bez  self też nie działa
    #dlaczego nie  mogę ustawić deafultowo jednego property
    