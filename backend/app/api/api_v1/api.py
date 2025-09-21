from fastapi import APIRouter
from app.api.api_v1.endpoints import chatbot, contact

api_router = APIRouter()

api_router.include_router(
    chatbot.router,
    prefix="/chatbot",
    tags=["chatbot"]
)

api_router.include_router(
    contact.router,
    prefix="/contact",
    tags=["contact"]
)