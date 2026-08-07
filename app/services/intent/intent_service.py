# app/services/intent/intent_service.py

from app.models.chat_intent import ChatIntent


class IntentService:

    def __init__(self):

        self.intents = {

            ChatIntent.GENERAL: [
                "hola",
                "buenas",
                "buenos dias",
                "buenas tardes",
                "buenas noches",
                "hey",
                "que tal",
                "cómo estás",
                "como estas",
                "gracias",
                "adiós",
                "adios",
                "hasta luego"
            ],

            ChatIntent.PROFILE: [
                "perfil",
                "información",
                "informacion",
                "quién eres",
                "quien eres",
                "quién es",
                "quien es",
                "háblame de ti",
                "hablame de ti",
                "sobre ti",
                "sobre él",
                "sobre el",
                "currículum",
                "cv",
                "presentate",
                "preséntate"
            ],

            ChatIntent.PROJECT: [
                "proyecto",
                "proyectos",
                "portafolio",
                "portfolio",
                "has hecho",
                "has desarrollado",
                "creaste",
                "desarrollaste"
            ],

            ChatIntent.CONTACT: [
                "correo",
                "email",
                "teléfono",
                "telefono",
                "contacto",
                "contactarte",
                "contactarlo",
                "linkedin",
                "celular",
                "whatsapp",
                "ubicación",
                "ubicacion",
                "dirección",
                "direccion"
            ],

            ChatIntent.EDUCATION: [
                "estudió",
                "estudio",
                "estudiaste",
                "universidad",
                "escuela",
                "educación",
                "educacion",
                "itescam",
                "ingeniería",
                "ingenieria",
                "carrera",
                "formación",
                "formacion"
            ],

            ChatIntent.EXPERIENCE: [
                "experiencia",
                "trabajo",
                "trabajaste",
                "has trabajado",
                "empresa",
                "plenumsoft",
                "laboral",
                "empleo",
                "cargo",
                "puesto"
            ],

            ChatIntent.SKILL: [
                "habilidades",
                "habilidad",
                "tecnologías",
                "tecnologias",
                "stack",
                "lenguajes",
                "sabes",
                "conoces",
                "manejas",
                "dominas"
            ],

            ChatIntent.CERTIFICATION: [
                "certificación",
                "certificacion",
                "certificaciones",
                "certificado",
                "curso",
                "diploma",
                "freecodecamp",
                "cisco",
                "kaggle"
            ],

            ChatIntent.GITHUB: [
                "github",
                "git hub",
                "perfil github",
                "perfil de github",
                "repositorio",
                "repositorios",
                "repos",
                "código",
                "codigo",
                "código fuente",
                "codigo fuente",
                "commit",
                "commits",
                "contribución",
                "contribuciones",
                "contribution",
                "git"
            ]

        }

        # Palabras específicas con pesos para resolver ambigüedad
        self.specific_keywords = {

            "react": ChatIntent.SKILL,
            "angular": ChatIntent.SKILL,
            "flutter": ChatIntent.SKILL,
            "python": ChatIntent.SKILL,
            "fastapi": ChatIntent.SKILL,
            "flask": ChatIntent.SKILL,
            "sql": ChatIntent.SKILL,

            "github": ChatIntent.GITHUB,
            "repositorio": ChatIntent.GITHUB,
            "repositorios": ChatIntent.GITHUB,
            "commit": ChatIntent.GITHUB,
            "commits": ChatIntent.GITHUB,
            "contribución": ChatIntent.GITHUB,
            "contribuciones": ChatIntent.GITHUB

        }

    def detect(self, question: str) -> ChatIntent:

        question = question.lower()

        scores = {}

        for intent, keywords in self.intents.items():

            score = 0

            for keyword in keywords:

                if keyword in question:
                    score += 1

            scores[intent] = score

        max_score = max(scores.values())

        if max_score == 0:
            return ChatIntent.UNKNOWN

        best_intents = [
            intent
            for intent, score in scores.items()
            if score == max_score
        ]

        if len(best_intents) > 1:

            for word, intent in self.specific_keywords.items():

                if word in question and intent in best_intents:
                    return intent

        return best_intents[0]