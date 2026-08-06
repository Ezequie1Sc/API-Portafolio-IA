# app/models/chat_intent.py
from enum import Enum

class ChatIntent(Enum):
    GENERAL = "general"        # NUEVO: Saludos y conversación casual
    PROFILE = "profile"
    PROJECT = "project"
    CONTACT = "contact"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    SKILL = "skill"
    CERTIFICATION = "certification"
    UNKNOWN = "unknown"