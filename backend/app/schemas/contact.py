from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactForm(BaseModel):
    """Schema for contact form submission"""
    name: str
    email: EmailStr
    subject: str
    message: str
    phone: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "subject": "Inquiry about your services",
                "message": "Hello, I would like to know more about your work.",
                "phone": "+1234567890"
            }
        }

class ContactResponse(BaseModel):
    """Schema for contact form response"""
    status: str
    message: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Thank you for your message. I will get back to you soon!"
            }
        }