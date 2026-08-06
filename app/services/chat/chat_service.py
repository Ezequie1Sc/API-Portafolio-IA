from app.services.intent.intent_service import IntentService

from app.services.knowledge.profile_service import ProfileService
from app.services.knowledge.contact_service import ContactService
from app.services.knowledge.education_service import EducationService
from app.services.knowledge.experience_service import ExperienceService
from app.services.knowledge.project_service import ProjectService
from app.services.knowledge.personality_service import PersonalityService

from app.models.chat_intent import ChatIntent


class ChatService:

    def __init__(self):

        self.intent_service = IntentService()

        self.profile_service = ProfileService()

        self.contact_service = ContactService()

        self.education_service = EducationService()

        self.experience_service = ExperienceService()

        self.project_service = ProjectService()

        self.personality_service = PersonalityService()