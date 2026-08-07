# app/models/chat_intent.py
from enum import Enum

class ChatIntent(Enum):
    GENERAL = "general"        
    PROFILE = "profile"
    PROJECT = "project"
    CONTACT = "contact"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    SKILL = "skill"    
    CERTIFICATION = "certification"
    GITHUB = "github"  
    UNKNOWN = "unknown"