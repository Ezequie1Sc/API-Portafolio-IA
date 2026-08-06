from enum import Enum


class ChatIntent(str, Enum):
    PROFILE = "profile"
    PROJECT = "project"
    CONTACT = "contact"
    EDUCATION = "education"
    EXPERIENCE = "experience"
    SKILL = "skill"
    CERTIFICATION = "certification"
    UNKNOWN = "unknown"