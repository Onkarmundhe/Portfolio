import sys
import os

# Get the backend directory (parent of parent of this file)
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add backend directory to Python path
sys.path.insert(0, backend_dir)

from main import app

# This is required for Vercel to find the ASGI application
app = app

