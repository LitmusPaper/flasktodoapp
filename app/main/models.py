from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean)
