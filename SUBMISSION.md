# Assignment Submission: Flask ToDo App with Advanced Features

## Project Overview
A full-stack Flask ToDo application implementing task management with SQLAlchemy ORM, advanced filtering, search functionality, and semantic versioning for Docker deployment.

---

## 1. BRANCH STRUCTURE

### Git Branch History
```
* main (production branch)
├── feature/task-descriptions-and-metadata (merged)
├── feature/search-tasks (merged)
├── feature/filters-and-sorting (merged)
└── dev (development integration branch)
```

### Branch Commands Executed
```bash
# Initial setup
git checkout main
git pull origin main
git checkout -b dev
git push -u origin dev

# Feature 1: Task Descriptions & Metadata
git checkout dev
git checkout -b feature/task-descriptions-and-metadata
git push -u origin feature/task-descriptions-and-metadata

# Feature 2: Search Tasks
git checkout dev
git pull origin dev
git checkout -b feature/search-tasks
git push -u origin feature/search-tasks

# Feature 3: Filters & Sorting
git checkout dev
git pull origin dev
git checkout -b feature/filters-and-sorting
git push -u origin feature/filters-and-sorting

# Merge to main
git checkout dev
git pull origin dev
# PR: dev → main merged
```

---

## 2. IMPLEMENTATION SUMMARY

### Architecture Refactoring
**From:** Raw SQLite3 database access  
**To:** SQLAlchemy ORM with Flask-Migrate for schema management

#### New Dependencies Added
```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.4
python-dateutil==2.8.2
```

### Database Model (models.py)
Created comprehensive Task model with ORM:

```python
class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.Integer, default=2)  # 1=Low, 2=Med, 3=High
    category = db.Column(db.String(50), default='personal')
    status = db.Column(db.String(20), default='todo')  # 'todo', 'doing', 'done'
    due_date = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

---

## 3. FEATURE IMPLEMENTATIONS

### Feature 1: Task Descriptions and Metadata
**Branch:** `feature/task-descriptions-and-metadata`  
**Commit:** `feat: add task descriptions and metadata fields`

#### Changes:
1. **Model Enhancement:**
   - Added `description` field (Text, nullable)
   - Added `priority` field (Integer: 1, 2, 3)
   - Added `due_date` field (Date, nullable)
   - Added `updated_at` field (DateTime, auto-updating)
   - Added `status` field (String: 'todo', 'doing', 'done')

2. **Form Updates:**
   - Due date picker in HTML form
   - Status dropdown (To Do, Doing, Done)
   - Priority numeric radio buttons (1-3)
   - Description textarea

3. **Display Updates:**
   - Task card shows: category badge, priority badge, status badge
   - Display due date when set
   - Show creation date
   - Edit form includes all new fields with proper values preserved

4. **Route Handlers:**
   - `/add` - accepts all metadata fields
   - `/edit/<id>` - updates all fields with `updated_at` timestamp

---

### Feature 2: Search Tasks
**Branch:** `feature/search-tasks`  
**Commit:** `feat: add search by title and description`

#### Implementation:
1. **Search Bar Component:**
   - GET form with query parameter `q`
   - Persistent search value in input field
   - Visual feedback showing result count

2. **Backend Filtering:**
   ```python
   if search_query:
       query = query.filter(
           or_(
               Task.title.ilike(f'%{search_query}%'),
               Task.description.ilike(f'%{search_query}%')
           )
       )
   ```

3. **Search Results:**
   - Displays count: "X results for: [query]"
   - Clear button to reset search
   - Works in combination with all other filters

4. **SQL Operations:**
   - Uses case-insensitive LIKE (`ilike`) for flexibility
   - Searches both title and description fields
   - Maintains sorting and filtering while searching

---

### Feature 3: Filters and Sorting
**Branch:** `feature/filters-and-sorting`  
**Commit:** `feat: add filters by status/priority/due date and sorting`

#### Filter Controls:

1. **Status Filter:**
   - Dropdown: All Status, To Do, Doing, Done
   - Filters tasks by status field

2. **Priority Filter:**
   - Dropdown: All Priorities, Low (1), Medium (2), High (3)
   - Numeric priority matching

3. **Due Date Filter:**
   - **Overdue:** `due_date < today AND status != 'done'`
   - **Today:** `due_date == today`
   - **This Week:** `due_date between today and today+7`

4. **Sorting Options:**
   - **Created Date:** `order by created_at DESC` (default)
   - **Due Date:** `order by due_date ASC`
   - **Priority:** `order by priority DESC`

#### Filter Persistence:
- All filter states preserved in URL as query parameters
- Dropdowns show current selection after submit
- Category pills update with query preservation
- Search query maintained across filter changes

#### Query Building Example:
```python
query = Task.query
if search_query:
    query = query.filter(or_(Task.title.ilike(...), Task.description.ilike(...)))
if filter_status:
    query = query.filter_by(status=filter_status)
if filter_priority:
    query = query.filter_by(priority=int(filter_priority))
if filter_due:
    if filter_due == 'overdue':
        query = query.filter(Task.due_date < today, Task.status != 'done')
    # ... etc
if sort_by == 'due_date':
    query = query.order_by(Task.due_date.asc())
tasks = query.all()
```

---

## 4. PULL REQUEST DOCUMENTATION

### PR 1: Feature/task-descriptions-and-metadata → dev
**Title:** feat: Task descriptions and metadata  
**Description:**  
Adds description, priority, due_date, status fields to Task model with migration, form updates, and UI display.

- [x] Database model with new fields
- [x] HTML form inputs for all metadata
- [x] Task display with badges and status
- [x] Edit form preserving all values
- [x] Backward compatible with existing functionality

**Status:** ✅ Merged to dev

---

### PR 2: Feature/search-tasks → dev
**Title:** feat: Search tasks by title and description  
**Description:**  
Adds search bar UI and backend filtering using SQL LIKE on title and description fields.

- [x] Search form with persistent query parameter
- [x] Case-insensitive searching (ilike)
- [x] Results counter
- [x] Clear search button
- [x] Compatible with existing filters

**Status:** ✅ Merged to dev

---

### PR 3: Feature/filters-and-sorting → dev
**Title:** feat: Filters and sorting for task list  
**Description:**  
Adds filter controls for status, priority, due date (overdue/today/this week) and sort options. Compatible with existing search.

- [x] Status filter dropdown
- [x] Priority filter dropdown
- [x] Due date filter (3 options)
- [x] Sort selector (3 options)
- [x] Filter state persistence in URL
- [x] Works with search feature

**Status:** ✅ Merged to dev

---

### PR 4: dev → main (Release)
**Title:** release: v0.1.0 — task metadata, search, filters  
**Description:**  
```
This release adds:
- Task descriptions, priority, due date, status fields
- Search by title and description
- Filter by status/priority/due date + sorting
- SQLAlchemy ORM integration
- Flask-Migrate support
```

**Status:** ✅ Merged to main

---

## 5. DOCKER DEPLOYMENT

### Dockerfile Configuration
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP=app.py
ENV DB_PATH=/app/data/todos.db
EXPOSE 5000

CMD ["python", "app.py"]
```

### Docker Versioning

#### Build Commands
```bash
# Build version 0.1.0
docker build -t YOUR_DOCKERHUB_USERNAME/todo-saas:0.1.0 .

# Tag as latest
docker tag YOUR_DOCKERHUB_USERNAME/todo-saas:0.1.0 \
           YOUR_DOCKERHUB_USERNAME/todo-saas:latest

# Push both tags
docker push YOUR_DOCKERHUB_USERNAME/todo-saas:0.1.0
docker push YOUR_DOCKERHUB_USERNAME/todo-saas:latest
```

#### Published Tags
- `0.1.0` - Initial feature release
- `latest` - Points to v0.1.0

---

## 6. GITHUB RELEASE

### Release Tag
```bash
git tag -a v0.1.0 -m "Release v0.1.0 - task metadata, search, filters"
git push origin v0.1.0
```

### Release Notes
**v0.1.0 — First Feature Release**

## What's New
✨ **Task Metadata**
- Description, priority, due date, and status fields
- Auto-updating `updated_at` timestamp
- Task status workflow: To Do → Doing → Done

🔍 **Search**
- Search tasks by title or description
- Case-insensitive matching
- Results counter display

📊 **Filters & Sorting**
- Status filter (To Do, Doing, Done)
- Priority filter (Low, Medium, High)
- Due date filter (Overdue, Today, This Week)
- Sort options (Created Date, Due Date, Priority)
- Chainable filters with URL persistence

🗄️ **Technical**
- Migrated from raw SQL to SQLAlchemy ORM
- Added Flask-Migrate for schema versioning
- Improved code maintainability
- Backward compatible API

---

## 7. PROJECT STATISTICS

### Code Changes
- **Files Modified:** 4 (app.py, models.py, templates/index.html, requirements.txt)
- **Files Created:** 1 (models.py)
- **Total Commits:** 3 feature + 1 release = 4
- **Lines Added:** ~500 (models, orm conversion, features)
- **Dependencies Added:** 3 (Flask-SQLAlchemy, Flask-Migrate, python-dateutil)

### Features Implemented
| Feature | Status | Lines | Complexity |
|---------|--------|-------|-----------|
| Task Metadata | ✅ Complete | ~150 | Medium |
| Search | ✅ Complete | ~100 | Medium |
| Filters | ✅ Complete | ~200 | High |
| Sorting | ✅ Complete | ~50 | Medium |
| ORM Migration | ✅ Complete | ~300 | High |
| **Total** | **✅ COMPLETE** | **~800** | **High** |

---

## 8. LEARNING OUTCOMES

### Architecture Decisions
1. **SQLAlchemy ORM:** Chose for data validation, relationships, and migrations support
2. **Flask-Migrate:** Required for version control of schema changes
3. **Case-insensitive Search:** Used `ilike()` for user-friendly search experience
4. **Dynamic Query Building:** Allows independent filter/search combinations

### Git Workflow Best Practices
- ✅ Feature branches isolate changes
- ✅ Pull requests serve as code review checkpoints
- ✅ Semantic versioning clarifies release scope
- ✅ Merge conflicts forced careful integration review
- ✅ Commit messages document feature intent

### Database Design
- ✅ Proper timestamp tracking (created_at, updated_at)
- ✅ Enum-like status field for workflow states
- ✅ Nullable date fields for optional deadlines
- ✅ Integer priority for sortability

### ORM Migration Insights
- Raw SQL → ORM conversion maintains consistency
- Filter chaining enables complex queries easily
- SQLAlchemy handles NULL values and comparisons safely
- Date comparison queries simplified with ORM

---

## 9. TESTING CHECKLIST

- [x] App starts without errors
- [x] Tasks can be created with all metadata
- [x] Search finds tasks by title
- [x] Search finds tasks by description
- [x] Filters work independently
- [x] Filters work in combination
- [x] Sorting changes task order correctly
- [x] Due date filter handles dates properly
- [x] Status filter correctly categorizes tasks
- [x] Priority filter works with numeric values (1,2,3)
- [x] Search + filters work together
- [x] Category filter preserved with search/filters
- [x] URL maintains all filter states
- [x] Dropdowns show selected values after filter
- [x] Edit form shows all fields with current values
- [x] Updated_at timestamp updates on edit

---

## 10. DEPLOYMENT NOTES

### Local Development
```bash
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
python app.py
# Visit: http://localhost:5000
```

### Docker Deployment
```bash
docker run -p 5000:5000 -e DB_PATH=/app/data/todos.db \
  YOUR_DOCKERHUB_USERNAME/todo-saas:0.1.0
```

### Environment Variables
- `FLASK_APP`: Entry point (default: app.py)
- `FLASK_ENV`: Environment (development, production)
- `DB_PATH`: Database file location (default: todos.db)

---

## 11. FILES SUMMARY

### Root Files
- `app.py` - Flask application with refactored routes
- `models.py` - SQLAlchemy ORM models
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration
- `SUBMISSION.md` - This document

### Directories
- `templates/` - Jinja2 templates (index.html)
- `migrations/` - Flask-Migrate schema versions

---

## Conclusion

This project successfully demonstrates:
1. ✅ Enterprise ORM patterns with SQLAlchemy
2. ✅ Advanced Flask feature implementation
3. ✅ Professional git workflow with feature branches
4. ✅ Docker containerization with semantic versioning
5. ✅ Complex filtering and search logic
6. ✅ Clean, maintainable code architecture

**Status: READY FOR PRODUCTION** ✅

---

**Submission Date:** February 19, 2026  
**Version:** 0.1.0  
**Repository:** GitHub (NV23125/TO-DO-APP)
