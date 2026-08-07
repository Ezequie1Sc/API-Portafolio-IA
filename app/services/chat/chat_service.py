# app/services/chat/chat_service.py

from app.models.chat_intent import ChatIntent
from app.services.intent.intent_service import IntentService
from app.services.ai.context_builder import ContextBuilder
from app.services.ai.gemini_service import GeminiService

from app.services.knowledge.profile_service import ProfileService
from app.services.knowledge.contact_service import ContactService
from app.services.knowledge.education_service import EducationService
from app.services.knowledge.experience_service import ExperienceService
from app.services.knowledge.project_service import ProjectService
from app.services.knowledge.skill_service import SkillService
from app.services.knowledge.certification_service import CertificationService
from app.services.knowledge.personality_service import PersonalityService
from app.services.knowledge.github_service import GithubService


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
        self.skill_service = SkillService()
        self.certification_service = CertificationService()
        self.personality_service = PersonalityService()
        self.github_service = GithubService()

        self.handlers = {

            ChatIntent.PROFILE: self.profile_service.get,

            ChatIntent.CONTACT: self.contact_service.get,

            ChatIntent.EDUCATION: self.education_service.get,

            ChatIntent.EXPERIENCE: self.experience_service.get,

            ChatIntent.PROJECT: self.project_service.search,

            ChatIntent.SKILL: self.skill_service.search,

            ChatIntent.CERTIFICATION: self.certification_service.search,

            ChatIntent.GITHUB: self.github_service.get

        }

    def process(self, question: str):

        intent = self.intent_service.detect(question)

        handler = self.handlers.get(intent)

        personality = self.personality_service.get()

        # =====================================
        # Conversación general
        # =====================================

        if intent == ChatIntent.GENERAL:

            prompt = self.context_builder.build(
                question=question,
                intent=ChatIntent.GENERAL,
                data={},
                personality=personality
            )

            return self.gemini_service.generate(prompt)

        # =====================================
        # Intent desconocido
        # =====================================

        if handler is None:

            prompt = self.context_builder.build(
                question=question,
                intent=ChatIntent.UNKNOWN,
                data={},
                personality=personality
            )

            return self.gemini_service.generate(prompt)

        # =====================================
        # Intents con información
        # =====================================

        try:

            if intent in (

                ChatIntent.PROJECT,

                ChatIntent.SKILL,

                ChatIntent.CERTIFICATION,

            ):

                data = handler(question)

            else:

                data = handler()

            prompt = self.context_builder.build(

                question=question,

                intent=intent,

                data=data,

                personality=personality

            )

            return self.gemini_service.generate(prompt)

        except Exception as e:

            print(e)

            prompt = self.context_builder.build(
                question=question,
                intent=ChatIntent.UNKNOWN,
                data={},
                personality=personality
            )

            return self.gemini_service.generate(prompt)