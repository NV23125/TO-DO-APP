from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from models import db, Task
from datetime import datetime, timedelta, date
from sqlalchemy import or_
import os

app = Flask(__name__)

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.getenv('DB_PATH', os.path.join(basedir, 'todos.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Create tables
with app.app_context():
    db.create_all()


@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description', '')
    priority = request.form.get('priority', '2')
    category = request.form.get('category', 'personal')
    status = request.form.get('status', 'todo')
    due_date = request.form.get('due_date', '')
    
    try:
        task = Task(
            title=title,
            description=description,
            priority=int(priority),
            category=category,
            status=status,
            due_date=datetime.strptime(due_date, '%Y-%m-%d').date() if due_date else None
        )
        db.session.add(task)
        db.session.commit()
    except Exception as e:
        print(f"Error adding task: {e}")
        db.session.rollback()
    
    return redirect(url_for('index'))

@app.route('/')
def index():
    # Get filter and search parameters
    filter_category = request.args.get('category', 'all')
    filter_status = request.args.get('status', '')
    filter_priority = request.args.get('priority', '')
    filter_due = request.args.get('due', '')
    sort_by = request.args.get('sort', 'created_date')
    search_query = request.args.get('q', '')
    
    # Start with base query
    query = Task.query
    
    # Apply search filter
    if search_query:
        query = query.filter(
            or_(
                Task.title.ilike(f'%{search_query}%'),
                Task.description.ilike(f'%{search_query}%')
            )
        )
    
    # Apply category filter
    if filter_category and filter_category != 'all':
        query = query.filter_by(category=filter_category)
    
    # Apply status filter
    if filter_status and filter_status != '':
        query = query.filter_by(status=filter_status)
    
    # Apply priority filter
    if filter_priority and filter_priority != '':
        query = query.filter_by(priority=int(filter_priority))
    
    # Apply due date filter
    today = date.today()
    if filter_due and filter_due != '':
        if filter_due == 'overdue':
            query = query.filter(Task.due_date < today, Task.status != 'done')
        elif filter_due == 'today':
            query = query.filter_by(due_date=today)
        elif filter_due == 'this_week':
            week_end = today + timedelta(days=7)
            query = query.filter(Task.due_date >= today, Task.due_date <= week_end)
    
    # Apply sorting
    if sort_by == 'due_date':
        query = query.order_by(Task.due_date.asc(), Task.created_at.desc())
    elif sort_by == 'priority':
        query = query.order_by(Task.priority.desc(), Task.created_at.desc())
    else:  # created_date (default)
        query = query.order_by(Task.created_at.desc())
    
    tasks = query.all()
    
    return render_template(
        'index.html',
        todos=tasks,
        current_category=filter_category,
        search_query=search_query,
        filter_status=filter_status,
        filter_priority=filter_priority,
        filter_due=filter_due,
        sort_by=sort_by
    )

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    task = Task.query.get_or_404(todo_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit_todo(todo_id):
    task = Task.query.get_or_404(todo_id)
    
    title = request.form.get('title')
    description = request.form.get('description', '')
    priority = request.form.get('priority', '2')
    category = request.form.get('category', 'personal')
    status = request.form.get('status', 'todo')
    due_date = request.form.get('due_date', '')
    
    try:
        task.title = title
        task.description = description
        task.priority = int(priority)
        task.category = category
        task.status = status
        task.due_date = datetime.strptime(due_date, '%Y-%m-%d').date() if due_date else None
        task.updated_at = datetime.utcnow()
        db.session.commit()
    except Exception as e:
        print(f"Error editing task: {e}")
        db.session.rollback()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    task = Task.query.get_or_404(todo_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)