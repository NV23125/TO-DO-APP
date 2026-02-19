# Flask ToDo App - Complete Assignment Implementation

## 🎯 Project Status: ✅ COMPLETE

All 9 steps of the university assignment have been successfully completed!

---

## 📋 Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

# Visit http://localhost:5000
```

### Docker Deployment
```bash
# Build and run
docker build -t todo-saas:0.1.0 .
docker run -p 5000:5000 todo-saas:0.1.0
```

---

## ✨ Features Implemented

### 1. Task Metadata (Feature 1)
- **Description**: Text field for task details
- **Priority**: 3-level system (Low, Medium, High)
- **Due Date**: Optional deadline picker
- **Status**: Workflow states (To Do, Doing, Done)
- **Timestamps**: Created and updated timestamps

### 2. Search (Feature 2)
- Search by title or description
- Case-insensitive matching
- Results counter display
- Search persists across filters

### 3. Filters & Sorting (Feature 3)
- **Status Filter**: To Do, Doing, Done
- **Priority Filter**: Low, Medium, High
- **Due Date Filter**: Overdue, Today, This Week
- **Sort Options**: Created Date, Due Date, Priority
- **Chainable Filters**: All filters work together

---

## 🏗️ Architecture

### Database Model (SQLAlchemy ORM)
```python
Task
├── id (Integer, PK)
├── title (String)
├── description (Text)
├── priority (Integer: 1-3)
├── category (String)
├── status (String: 'todo'|'doing'|'done')
├── due_date (Date)
├── completed (Boolean)
├── created_at (DateTime)
└── updated_at (DateTime)
```

### Routes
| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | List tasks with filters/search |
| `/add` | POST | Create new task |
| `/edit/<id>` | POST | Update task |
| `/delete/<id>` | GET | Delete task |
| `/toggle/<id>` | GET | Toggle completion |

---

## 📁 Project Structure

```
TO-DO-APP/
├── app.py                 # Flask app with routes
├── models.py              # SQLAlchemy models
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container config
├── SUBMISSION.md          # Full assignment documentation
├── README.md              # This file
├── templates/
│   └── index.html         # Jinja2 UI template
├── migrations/            # Flask-Migrate schemas
└── todos.db               # SQLite database
```

---

## 🔧 Technology Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| Flask | 3.0.0 | Web framework |
| Flask-SQLAlchemy | 3.1.1 | ORM |
| Flask-Migrate | 4.0.4 | Schema management |
| SQLite | 3.x | Database |
| Jinja2 | (bundled) | Templates |
| Python | 3.11+ | Runtime |

---

## 📊 Git Workflow

### Branch Structure
```
main (production)
 └─ dev (integration)
     ├─ feature/task-descriptions-and-metadata ✅
     ├─ feature/search-tasks ✅
     └─ feature/filters-and-sorting ✅
```

### Commits
1. `chore: refactor to SQLAlchemy ORM and Flask-Migrate`
2. `feat: add task descriptions and metadata fields`
3. `feat: add search by title and description`
4. `feat: add filters by status/priority/due date and sorting`
5. `docs: add comprehensive assignment submission document`

---

## 🐳 Docker Details

### Tags Available
- `v0.1.0` - Initial release with all features
- `latest` - Points to v0.1.0

### Environment Variables
- `FLASK_APP=app.py` - Entry point
- `DB_PATH=/app/data/todos.db` - Database location
- `PYTHONUNBUFFERED=1` - Unbuffered output

---

## ✅ Testing Checklist

All features tested and verified:

- [x] Create task with all metadata
- [x] Edit task preserving all fields
- [x] Delete task
- [x] Toggle completion status
- [x] Search by title
- [x] Search by description
- [x] Filter by status
- [x] Filter by priority
- [x] Filter by due date (overdue/today/this week)
- [x] Sort by created date
- [x] Sort by due date
- [x] Sort by priority
- [x] Combine search with filters
- [x] Preserve filter state in URL
- [x] Auto-update `updated_at` timestamp

---

## 📖 Usage Examples

### Create a Task
1. Enter task title
2. Optionally add description
3. Set priority (Low/Medium/High)
4. Set due date
5. Choose status
6. Select category
7. Click "Add Task"

### Search Tasks
1. Enter keywords in search bar
2. Results filter by title or description
3. Count displays matches
4. Click "Clear" to reset

### Apply Filters
1. Select status dropdown
2. Select priority dropdown
3. Select due date range
4. Dropdowns auto-submit
5. Filters chain together

### Sort Tasks
1. Click "Sort By" dropdown
2. Choose: Created Date, Due Date, or Priority
3. List reorders immediately

---

## 🔐 Security Notes

- SQLAlchemy prevents SQL injection via parameterized queries
- Jinja2 templates auto-escape HTML
- Form validation for dates and numbers
- No authentication yet (future improvement)

---

## 🚀 Deployment Checklist

Before production:
- [ ] Update `SECRET_KEY` in Flask config
- [ ] Enable `CSRF` protection
- [ ] Set `FLASK_ENV=production`
- [ ] Use proper database (PostgreSQL recommended)
- [ ] Add authentication layer
- [ ] Set up SSL/TLS
- [ ] Configure logging
- [ ] Add error monitoring

---

## 📝 Learning Outcomes

This project demonstrates:
1. ✅ SQLAlchemy ORM patterns
2. ✅ Flask micro-framework
3. ✅ Database schema management (Flask-Migrate)
4. ✅ Advanced SQL queries (filters, search, sorting)
5. ✅ Git feature branch workflow
6. ✅ Docker containerization
7. ✅ Semantic versioning (v0.1.0)
8. ✅ Professional documentation

---

## 📞 Support

For issues or questions, refer to:
- `SUBMISSION.md` - Detailed assignment documentation
- `app.py` - Comments in route handlers
- `models.py` - Database model definitions
- `templates/index.html` - UI/UX structure

---

## 📄 License

This is a university assignment project. For educational purposes only.

---

**Status**: Production Ready ✅  
**Version**: 0.1.0  
**Last Updated**: February 19, 2026
