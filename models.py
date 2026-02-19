from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum as PyEnum

db = SQLAlchemy()

class TaskStatus(PyEnum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.Integer, default=2)  # 1=Low, 2=Medium, 3=High
    category = db.Column(db.String(50), default='personal')
    status = db.Column(db.String(20), default='todo')  # 'todo', 'doing', 'done'
    due_date = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'category': self.category,
            'status': self.status,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
