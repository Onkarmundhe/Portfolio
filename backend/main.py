from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.core.email import warm_smtp_connection
import re

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Pre-warm SMTP connection
    print("🚀 Starting Portfolio API...")
    try:
        # Only warm SMTP if credentials are configured
        if settings.SMTP_HOST and settings.SMTP_USERNAME:
            warm_smtp_connection()
        else:
            print("⚠️  SMTP not configured, skipping warm-up")
    except Exception as e:
        print(f"⚠️  SMTP warm-up failed: {e}")
    yield
    # Shutdown: Clean up if needed
    print("👋 Shutting down Portfolio API...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Custom CORS origin validator
def is_allowed_origin(origin: str) -> bool:
    if origin in settings.BACKEND_CORS_ORIGINS:
        return True
    
    # Allow all Vercel preview deployments
    if re.match(r"https://.*\.vercel\.app$", origin):
        return True
    
    # Allow all Netlify preview deployments
    if re.match(r"https://.*\.netlify\.app$", origin):
        return True
    
    return False

# Set up CORS middleware with allow_origin_regex
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://.*\.(vercel|netlify)\.app$",
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to Portfolio API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)