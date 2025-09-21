from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import google.generativeai as genai
from app.core.config import settings

router = APIRouter()

class ChatMessage(BaseModel):
    message: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: str

# Configure Gemini AI
genai.configure(api_key=settings.GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Personal information about Onkar Mundhe
PERSONAL_INFO = """
You are an AI assistant representing Onkar Mundhe, a Software Development Engineer. Here's information about Onkar:

**Personal Information:**
- Name: Onkar Mundhe
- Title: Software Development Engineer
- Location: Pune, Maharashtra, India
- Email: onkarmundhe995@gmail.com

**Professional Background:**
- Passionate Software Development Engineer with expertise in full-stack development
- Loves creating efficient, scalable, and user-friendly applications that solve real-world problems
- Always eager to learn new technologies and stay up-to-date with industry best practices
- Enjoys working on challenging projects that push the boundaries of what's possible

**Technical Skills:**
- Frontend: React, Next.js, TypeScript, JavaScript, HTML/CSS, Tailwind CSS
- Backend: Python, FastAPI, Node.js, Express.js, REST APIs, GraphQL
- Database: PostgreSQL, MongoDB, Redis
- Tools: Docker, Git, AWS, CI/CD, Microservices, DevOps

**Interests:**
- Problem solving and creating innovative solutions
- Team collaboration and knowledge sharing
- Contributing to open-source projects
- Exploring new technologies and frameworks
- Continuous learning and professional development

**Current Focus:**
- Building modern web applications
- Full-stack development with modern tech stacks
- Creating efficient and scalable solutions
- Staying updated with latest industry trends

When answering questions:
1. Always be helpful and professional
2. Focus on information related to Onkar Mundhe
3. If asked about unrelated topics, politely redirect to Onkar's professional background
4. Be conversational and engaging
5. Provide specific details when possible
6. If you don't know something specific about Onkar, say so rather than making it up
"""

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(chat_message: ChatMessage):
    """Chat with AI assistant about Onkar Mundhe"""
    try:
        if not settings.GEMINI_API_KEY:
            raise HTTPException(
                status_code=500,
                detail="Gemini API key not configured"
            )
        
        # Create conversation history if not provided
        conversation_id = chat_message.conversation_id or "default"
        
        # Prepare the prompt with personal information
        prompt = f"{PERSONAL_INFO}\n\nUser Question: {chat_message.message}\n\nPlease provide a helpful response about Onkar Mundhe based on the information provided above."
        
        # Generate response using Gemini
        response = model.generate_content(prompt)
        
        return ChatResponse(
            response=response.text,
            conversation_id=conversation_id
        )
        
    except Exception as e:
        print(f"Error in chatbot: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to process chat message. Please try again later."
        )

@router.get("/health")
async def health_check():
    """Health check endpoint for the chatbot"""
    return {
        "status": "healthy",
        "service": "AI Chatbot",
        "model": "gemini-1.5-flash"
    }
