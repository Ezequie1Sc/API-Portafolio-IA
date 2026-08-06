from app.models.chat_intent import ChatIntent


class IntentService:

    def __init__(self):

        self.intents = {

            ChatIntent.PROFILE: [
                "perfil",
                "información",
                "informacion",
                "quién es",
                "quien es",
                "háblame",
                "hablame",
                "sobre él",
                "sobre el",
                "currículum",
                "cv"
            ],

            ChatIntent.PROJECT: [
                "proyecto",
                "proyectos",
                "react",
                "angular",
                "flutter",
                "fastapi",
                "flask",
                "api",
                "backend",
                "frontend",
                "portafolio",
                "sistema",
                "aplicación",
                "aplicacion"
            ],

            ChatIntent.CONTACT: [
                "correo",
                "email",
                "teléfono",
                "telefono",
                "contacto",
                "github",
                "linkedin",
                "linkedin",
                "celular",
                "whatsapp"
            ],

            ChatIntent.EDUCATION: [
                "estudió",
                "estudio",
                "universidad",
                "escuela",
                "educación",
                "educacion",
                "itescam",
                "ingeniería",
                "ingenieria"
            ],

            ChatIntent.EXPERIENCE: [
                "experiencia",
                "trabajo",
                "empresa",
                "plenumsoft",
                "laboral",
                "empleo"
            ],

            ChatIntent.SKILL: [
                "habilidades",
                "tecnologías",
                "tecnologias",
                "stack",
                "lenguajes",
                "python",
                "react",
                "sql",
                "flutter"
            ],

            ChatIntent.CERTIFICATION: [
                "certificación",
                "certificacion",
                "certificaciones",
                "curso",
                "diploma",
                "freecodecamp",
                "cisco",
                "kaggle"
            ]

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

        best_intent = max(scores, key=scores.get)

        if scores[best_intent] == 0:
            return ChatIntent.UNKNOWN

        return best_intent