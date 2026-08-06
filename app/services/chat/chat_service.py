from app.models.chat_intent import ChatIntent

from app.services.intent.intent_service import IntentService

from app.services.ai.context_builder import ContextBuilder
from app.services.ai.gemini_service import GeminiService

from app.services.knowledge.profile_service import ProfileService
from app.services.knowledge.contact_service import ContactService
from app.services.knowledge.education_service import EducationService
from app.services.knowledge.experience_service import ExperienceService
from app.services.knowledge.project_service import ProjectService
from app.services.knowledge.personality_service import PersonalityService


class ChatService:

    def __init__(self):

        self.intent_service = IntentService()

        self.context_builder = ContextBuilder()

        self.gemini_service = GeminiService()

        self.profile_service = ProfileService()
        self.contact_service = ContactService()
        self.education_service = EducationService()
        self.experience_service = ExperienceService()
        self.project_service = ProjectService()

        self.personality_service = PersonalityService()

        self.handlers = {

            ChatIntent.PROFILE: self.profile_service.get,

            ChatIntent.CONTACT: self.contact_service.get,

            ChatIntent.EDUCATION: self.education_service.get,

            ChatIntent.EXPERIENCE: self.experience_service.get,

            ChatIntent.PROJECT: self.project_service.search

        }

    def process(self, question: str):

        intent = self.intent_service.detect(question)

        handler = self.handlers.get(intent)

        if handler is None:

            return "Lo siento, no encontré información relacionada."

        # ProjectService necesita la pregunta
        if intent == ChatIntent.PROJECT:

            data = handler(question)

        else:

            data = handler()

        personality = self.personality_service.get()

        prompt = self.context_builder.build(

            question=question,

            intent=intent,

            data=data,

            personality=personality

        )

        response = self.gemini_service.generate(prompt)

        return response