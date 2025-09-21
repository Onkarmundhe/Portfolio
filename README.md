# Modern Portfolio Website

A modern portfolio website built with Next.js and FastAPI.

## Tech Stack

### Frontend
- Next.js 14
- TypeScript
- TailwindCSS
- ESLint

### Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL

## Project Structure

```
├── frontend/           # Next.js frontend application
└── backend/            # FastAPI backend application
```

## Getting Started

### Frontend Setup
1. Navigate to the frontend directory
2. Install dependencies: `npm install`
3. Run development server: `npm run dev`

### Backend Setup
1. Navigate to the backend directory
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: 
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run development server: `uvicorn main:app --reload`