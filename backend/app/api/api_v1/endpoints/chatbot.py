from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import google.generativeai as genai
from app.core.config import settings
import json
import os

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

# Load Onkar's data from JSON file
def load_onkar_data():
    """Load Onkar's data from the JSON file"""
    try:
        # Get the path to the JSON file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "..", "..", "..", "data", "onkar_data.json")
        
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    except Exception as e:
        print(f"Error loading Onkar data: {e}")
        return {"personal_info": {"name": "Onkar Mundhe"}, "projects": []}

# Load the data once when the module is imported
ONKAR_DATA = load_onkar_data()

def get_relevant_data(message: str) -> str:
    """
    Analyze the message and return relevant data sections
    """
    message_lower = message.lower()
    
    # Check if question is about work experience/career
    work_keywords = ['work', 'job', 'career', 'experience', 'employment', 'company', 'position', 'role', 'intern', 'internship', 'predusk', 'current job', 'working', 'worked']
    if any(keyword in message_lower for keyword in work_keywords):
        return json.dumps({
            "work_experience": ONKAR_DATA.get("work_experience", []),
            "personal_info": ONKAR_DATA["personal_info"],
            "professional_background": ONKAR_DATA["professional_background"]
        }, indent=2)
    
    # Check if question is about projects
    project_keywords = ['project', 'projects', 'github', 'repository', 'typing', 'pdf', 'analyzer', 'scheduling', 'built', 'created', 'developed']
    if any(keyword in message_lower for keyword in project_keywords):
        return json.dumps({
            "projects": ONKAR_DATA["projects"],
            "technical_skills": ONKAR_DATA["technical_skills"]
        }, indent=2)
    
    # Check if question is about skills/technologies
    skill_keywords = ['skill', 'skills', 'technology', 'technologies', 'programming', 'language', 'framework', 'tool', 'database']
    if any(keyword in message_lower for keyword in skill_keywords):
        return json.dumps({
            "technical_skills": ONKAR_DATA["technical_skills"],
            "projects": [{"title": p["title"], "technologies": p["technologies"]} for p in ONKAR_DATA["projects"]]
        }, indent=2)
    
    # Check if question is about personal/contact info
    personal_keywords = ['contact', 'email', 'location', 'where', 'live', 'based', 'name', 'who']
    if any(keyword in message_lower for keyword in personal_keywords):
        return json.dumps({
            "personal_info": ONKAR_DATA["personal_info"],
            "professional_background": ONKAR_DATA["professional_background"]
        }, indent=2)
    
    # Default: return basic info
    return json.dumps({
        "personal_info": ONKAR_DATA["personal_info"],
        "professional_background": ONKAR_DATA["professional_background"],
        "current_focus": ONKAR_DATA["current_focus"]
    }, indent=2)

# Concise prompt that references the JSON data
SYSTEM_PROMPT = """
You are an AI assistant representing Onkar Mundhe, a Software Development Engineer from Pune, India.

IMPORTANT INSTRUCTIONS:
1. Use ONLY the provided JSON data to answer questions about Onkar
2. For questions NOT related to Onkar Mundhe, his work, skills, or experience, respond EXACTLY with: "Sorry, I can't answer about this. I am an AI assistant to answer about Onkar's work, skills, or experience."
3. Be conversational, professional, and confident in your responses
4. Answer questions naturally as if you are speaking about Onkar directly - NEVER use phrases like "according to the data", "as listed", "the information provided shows", "based on the information provided", "the data shows", or any similar references to data sources
5. Speak confidently about Onkar's background, skills, and experience as if you know him personally
6. For project questions, include technologies, descriptions, and GitHub links
7. If information isn't in the provided data, say you don't have that specific information
8. When mentioning locations, speak naturally (e.g., "His hometown is..." or "He's from..." rather than "His location is listed as...")
9. NEVER mention "information provided" or reference any data sources in your responses - speak directly and naturally

The relevant data for this question will be provided below.
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
        
        # Get relevant data based on the question type
        relevant_data = get_relevant_data(chat_message.message)
        
        # Create the full prompt with system instructions and relevant JSON data
        full_prompt = f"{SYSTEM_PROMPT}\n\nRelevant Data:\n{relevant_data}\n\nUser: {chat_message.message}\nAssistant:"
        
        # Generate response using Gemini
        response = model.generate_content(full_prompt)
        
        # Extract the response text
        response_text = response.text if response.text else "I'm sorry, I couldn't generate a response."
        
        return ChatResponse(
            response=response_text,
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
