## -------------------- Emil Ferent, Sep 2024 ---------------------
# the Model pattern

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True) #could also be alphanumeric
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # solar, wind, energy storage, etc.
    status = db.Column(db.String(50), default='under review')  # under review, in development, implemented
    submitter = db.Column(db.String(50), nullable=False) # person name
    created_at = db.Column(db.DateTime, default=datetime.utcnow) #timestamp, todo: change utcnow -> deprecated; works for now; also from Comment class

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer, db.ForeignKey('idea.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    idea = db.relationship('Idea', backref=db.backref('comments', lazy=True))
