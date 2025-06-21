# MCB Archives Backend

A FastAPI backend for serving archived radio shows for the MCB Archives project. Provides a public API for browsing, streaming, and downloading archived radio content.

## Quick Start

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows (bash)
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn[standard]
   ```
3. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

## Project Structure
- `main.py` — FastAPI app entry point
- `.gitignore` — Files and folders to exclude from git
- `README.md` — Project info and setup instructions
