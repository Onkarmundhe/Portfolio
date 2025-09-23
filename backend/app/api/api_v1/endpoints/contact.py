from fastapi import APIRouter, HTTPException
from app.schemas.contact import ContactForm
from app.core.email import send_email

router = APIRouter()

@router.post("/send")
async def send_contact_form(contact: ContactForm):
    """Send contact form email"""
    try:
        # Send email using the contact form data
        email_sent = await send_email(
            to_email=contact.email,  # This parameter exists but we send to our own email
            subject=contact.subject,
            message=contact.message,
            from_name=contact.name,
            from_email=contact.email
        )
        
        if email_sent:
            return {
                "status": "success",
                "message": "Thank you for your message. I will get back to you soon!"
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to send email. Please try again later."
            )
            
    except Exception as e:
        print(f"Error in contact form: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to send message. Please try again later."
        )