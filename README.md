# MCB Archives Backend

A FastAPI backend for serving archived radio shows for the MCB Archives project. Provides a public API for browsing, streaming, and downloading archived radio content.

## Quick Start

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv mcb-archives-backend
   source mcb-archives-backend/Scripts/activate  # On Windows (bash)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your database:
   - For development, SQLite is used by default.
   - For production, set up a PostgreSQL database (e.g., on Railway) and update your `.env` file with the connection string:
     ```env
     DATABASE_URL=postgresql+asyncpg://username:password@host:port/dbname
     ```
   - Install the async PostgreSQL driver:
     ```bash
     pip install asyncpg
     ```
4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables
- `DATABASE_URL`: The PostgreSQL database connection string

## Project Structure
```
mcb-archives-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app instance and routes
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas
│   └── database.py     # DB connection/session
│
├── .env
├── requirements.txt
├── README.md
├── .gitignore
```
