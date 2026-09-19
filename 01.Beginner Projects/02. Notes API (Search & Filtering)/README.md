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
