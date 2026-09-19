# Notes API 📝

A standalone FastAPI backend for note management with advanced search, filtering, and tagging.

## Features

- ✅ Full CRUD operations for notes
- 🔍 **Full-text search** across title and content
- 🏷️ **Tag system** with filter and autocomplete
- 📌 **Pinning** important notes to the top
- 📦 **Archiving** (soft delete) for recoverable deletion
- 📅 **Date range filtering**
- 🔄 **Flexible sorting** (created_at, updated_at, title)
- 📊 **Pagination with metadata** (total, skip, limit)
- 🎯 **Type-safe** with Pydantic v2

## Quick Start

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn app.main:app --reload

# 4. Open API docs
# http://127.0.0.1:8000/docs
```
## API Endpoints
----------------------------------
|Method	| Endpoint |	Description|
----------------------------------
|POST	| /api/v1/notes |	Create a new note |
|GET	|/api/v1/notes |	List notes with filters|
|GET	|/api/v1/notes/tags	| Get all unique tags|
|GET	|/api/v1/notes/{id} |	Get a specific note|
|PUT	|/api/v1/notes/{id} |	Update a note|
|PATCH	|/api/v1/notes/{id}/archive |	Archive (soft delete)|
|DELETE	|/api/v1/notes/{id}	|Permanently delete|
----------------------------------
## Advanced Filtering Examples
```bash
# Search notes containing "python"
GET /api/v1/notes?search=python

# Filter by multiple tags (OR logic)
GET /api/v1/notes?tags=work&tags=urgent

# Get pinned notes only
GET /api/v1/notes?is_pinned=true

# Date range filter
GET /api/v1/notes?start_date=2024-01-01T00:00:00&end_date=2024-12-31T23:59:59

# Sort alphabetically
GET /api/v1/notes?sort_by=title&sort_order=asc

# Combined filters
GET /api/v1/notes?search=python&tags=tutorial&is_pinned=true&sort_by=created_at
```
## Architecture
```text
Client → Router → CRUD → Model → Database
         ↓        ↓       ↓
      Schemas  Schemas  Schemas
     (Validate) (Logic)  (ORM)
Routers (api/): HTTP concerns

CRUD (crud/): Business logic

Models (models/): Database schema

Schemas (schemas/): Data validation
```

## Tech Stack
FastAPI - Web framework

SQLAlchemy 2.0 - ORM

Pydantic v2 - Data validation

SQLite - Database (dev)

Uvicorn - ASGI server
