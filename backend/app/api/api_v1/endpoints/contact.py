from fastapi import APIRouter, HTTPException
from app.schemas.contact import ContactForm
from app.core.email import send_email

router = APIRouter()

@router.post("/send")
async def send_contact_form(contact: ContactForm):
    """Send contact form email"""
    try:
        # Here you would typically implement email sending logic
        # For now, we'll just return a success message
        return {
            "status": "success",
            "message": "Thank you for your message. I will get back to you soon!"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to send message. Please try again later."
        )