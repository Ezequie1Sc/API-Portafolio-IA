import unicodedata

from app.models.chat_intent import ChatIntent


class IntentService:

    def __init__(self):

        # ==========================================================
        # PALABRAS Y FRASES CLAVE POR INTENCIÓN
        # ==========================================================

        self.intents = {

            # ======================================================
            # GENERAL
            # ======================================================

            ChatIntent.GENERAL: [
                "hola",
                "holaa",
                "holaaa",
                "ola",
                "olaaa",
                "buenas",
                "buenos dias",
                "buenas tardes",
                "buenas noches",
                "hey",
                "heyy",
                "que tal",
                "que onda",
                "que hay",
                "como estas",
                "como esta",
                "como te va",
                "como vas",
                "gracias",
                "muchas gracias",
                "gracias por ayudar",
                "te agradezco",
                "adios",
                "adioss",
                "hasta luego",
                "nos vemos",
                "bye",
                "chao",
            ],

            # ======================================================
            # PROFILE
            # ======================================================

            ChatIntent.PROFILE: [
                "perfil",
                "mi perfil",
                "tu perfil",
                "su perfil",
                "perfil profesional",

                "informacion sobre ti",
                "informacion de ti",
                "informacion personal",
                "informacion profesional",

                "quien eres",
                "quien es",
                "quien eres tu",
                "quien es el",
                "quien eres tu",

                "hablame de ti",
                "hablame sobre ti",
                "habla de ti",
                "cuentame de ti",
                "cuentame sobre ti",
                "dime sobre ti",

                "sobre ti",
                "sobre el",
                "sobre ezequiel",

                "presentate",
                "presentate tu",
                "presentacion",

                "conocerte",
                "conocerte mejor",
                "conocerlo",

                "curriculum",
                "curriculum vitae",
                "cv",
                "hoja de vida",

                "quien es ezequiel",
                "quien es ezequie1",
                "quien es ezequiel salazar",

                "ezequiel salazar",
                "ezequie1sc",
            ],

            # ======================================================
            # PROJECT
            # ======================================================

            ChatIntent.PROJECT: [
                "proyecto",
                "proyectos",
                "proyectoo",
                "proyectoss",

                "portafolio",
                "portafolio web",
                "portfolio",
                "portfolio web",

                "que has hecho",
                "que haz hecho",
                "que has desarrollado",
                "que haz desarrollado",

                "has hecho",
                "haz hecho",

                "has desarrollado",
                "haz desarrollado",

                "creaste",
                "creastes",
                "desarrollaste",
                "desarrollastes",

                "trabajos",
                "trabajo realizado",

                "proyectos realizados",
                "proyectos personales",
                "proyectos academicos",
            ],

            # ======================================================
            # CONTACT
            # ======================================================

            ChatIntent.CONTACT: [
                "correo",
                "correoo",
                "correo electronico",

                "email",
                "e mail",
                "mail",

                "telefono",
                "tel",
                "celular",
                "numero",
                "numero de telefono",
                "num de telefono",

                "contacto",
                "contactame",
                "contactarme",
                "contactarte",
                "contactarlo",
                "como contactarte",
                "como contacto",

                "linkedin",
                "linkeding",
                "linkdin",
                "linked in",

                "whatsapp",
                "whats app",
                "watsapp",
                "wasap",

                "ubicacion",
                "donde vives",
                "donde vive",
                "donde estas",
                "donde esta",

                "direccion",

                "como comunicarme",
                "como comunicarme contigo",
                "forma de contacto",
                "formas de contacto",
            ],

            # ======================================================
            # EDUCATION
            # ======================================================

            ChatIntent.EDUCATION: [
                "estudio",
                "estudias",
                "estudiaste",
                "estudio universitario",
                "estudios",

                "universidad",
                "universidad donde estudias",
                "universidad estudias",

                "escuela",
                "escuela donde estudias",

                "educacion",
                "educacion academica",
                "formacion",
                "formacion academica",

                "itescam",
                "itescan",

                "ingenieria",
                "ingeniero",
                "ingenieria en sistemas",
                "ingenieria de sistemas",

                "carrera",
                "carrera universitaria",

                "que estudias",
                "que estudiaste",
                "donde estudias",
                "donde estudiaste",

                "grado",
                "titulo",
                "titulo universitario",
            ],

            # ======================================================
            # EXPERIENCE
            # ======================================================

            ChatIntent.EXPERIENCE: [
                "experiencia",
                "experiencia profesional",
                "experiencia laboral",

                "trabajo",
                "trabajos",
                "trabajaste",
                "trabajas",
                "trabajado",

                "has trabajado",
                "haz trabajado",

                "empresa",
                "empresas",

                "plenumsoft",
                "plenum",
                "plenum soft",

                "laboral",
                "empleo",
                "empleos",

                "cargo",
                "puesto",
                "puesto de trabajo",

                "experiencia como desarrollador",
                "experiencia como programador",

                "donde trabajas",
                "donde trabajaste",

                "en que trabajas",
                "en que has trabajado",
            ],

            # ======================================================
            # SKILLS
            # ======================================================

            ChatIntent.SKILL: [

                # --------------------------------------------------
                # TECNOLOGÍAS
                # --------------------------------------------------

                "tecnologia",
                "tecnologias",

                "tecnolojia",
                "tecnolojias",
                "tecnoligia",
                "tecnoligias",
                "tecnlogia",
                "tecnlogias",
                "tecnolgia",

                "cuales son sus tecnologias",
                "cuales son tus tecnologias",

                "que tecnologias maneja",
                "que tecnologias manejas",

                "que tecnologia maneja",
                "que tecnologia manejas",

                "que tecnologias utiliza",
                "que tecnologias utilizas",

                "que tecnologia utiliza",
                "que tecnologia utilizas",

                "que tecnologias conoce",
                "que tecnologias conoces",

                "que tecnologia conoce",
                "que tecnologia conoces",

                "que tecnologias usa",
                "que tecnologias usas",

                "que tecnologia usa",
                "que tecnologia usas",

                "con que tecnologias trabaja",
                "con que tecnologias trabajas",

                "con que tecnologia trabaja",
                "con que tecnologia trabajas",

                # --------------------------------------------------
                # ¿QUÉ SABE HACER?
                # --------------------------------------------------

                "que sabe hacer",
                "que sabes hacer",

                "que sabe",
                "que sabes",

                "que puede hacer",
                "que puedes hacer",

                "que cosas sabe hacer",
                "que cosas sabes hacer",

                "que sabe desarrollar",
                "que sabes desarrollar",

                "que puede desarrollar",
                "que puedes desarrollar",

                "que sabe programar",
                "que sabes programar",

                "que puede programar",
                "que puedes programar",

                "que hace",
                "que haces",

                "que tipo de cosas hace",
                "que tipo de cosas haces",

                # --------------------------------------------------
                # HABILIDADES
                # --------------------------------------------------

                "habilidad",
                "habilidades",
                "habilidades tecnicas",
                "habilidades tecnologicas",

                "skill",
                "skills",
                "skil",
                "skils",

                "que habilidades tiene",
                "que habilidades tienes",

                "cuales son sus habilidades",
                "cuales son tus habilidades",

                "que conocimientos tiene",
                "que conocimientos tienes",

                "cuales son sus conocimientos",
                "cuales son tus conocimientos",

                "en que es bueno",
                "en que eres bueno",

                "en que tiene experiencia",
                "en que tienes experiencia",

                "que domina",
                "que dominas",

                "que cosas domina",
                "que cosas dominas",

                # --------------------------------------------------
                # LENGUAJES
                # --------------------------------------------------

                "lenguaje",
                "lenguajes",
                "lenguajes de programacion",

                "que lenguajes maneja",
                "que lenguajes manejas",

                "que lenguajes conoce",
                "que lenguajes conoces",

                "que lenguajes utiliza",
                "que lenguajes utilizas",

                "que lenguajes usa",
                "que lenguajes usas",

                "que lenguajes sabe",
                "que lenguajes sabes",

                "que lenguaje maneja",
                "que lenguaje manejas",

                # --------------------------------------------------
                # HERRAMIENTAS
                # --------------------------------------------------

                "herramienta",
                "herramientas",

                "que herramientas maneja",
                "que herramientas manejas",

                "que herramientas utiliza",
                "que herramientas utilizas",

                "que herramientas usa",
                "que herramientas usas",

                "que programas utiliza",
                "que programas utilizas",

                "que programas maneja",
                "que programas manejas",

                # --------------------------------------------------
                # FRAMEWORKS
                # --------------------------------------------------

                "framework",
                "frameworks",

                "que frameworks maneja",
                "que frameworks manejas",

                "que frameworks conoce",
                "que frameworks conoces",

                "que frameworks utiliza",
                "que frameworks utilizas",

                # --------------------------------------------------
                # STACK
                # --------------------------------------------------

                "stack",
                "stack tecnologico",
                "stack de tecnologias",
                "stack de tecnologia",
                "tech stack",
                "techstack",

                "cual es su stack",
                "cual es tu stack",

                "cual es su stack tecnologico",
                "cual es tu stack tecnologico",

                "que stack maneja",
                "que stack manejas",

                # --------------------------------------------------
                # PROGRAMACIÓN
                # --------------------------------------------------

                "programacion",
                "programador",
                "programador junior",

                "que sabe de programacion",
                "que sabes de programacion",

                "que conocimientos tiene de programacion",
                "que conocimientos tienes de programacion",

                "que experiencia tiene programando",
                "que experiencia tienes programando",

                "que sabe de desarrollo",
                "que sabes de desarrollo",

                # --------------------------------------------------
                # DESARROLLO
                # --------------------------------------------------

                "desarrollo web",
                "desarrollo backend",
                "desarrollo frontend",
                "desarrollo movil",

                "que tipo de aplicaciones desarrolla",
                "que tipo de aplicaciones desarrollas",

                "que aplicaciones hace",
                "que aplicaciones haces",

                "que aplicaciones puede desarrollar",
                "que aplicaciones puedes desarrollar",

                "que paginas web hace",
                "que paginas web haces",

                # --------------------------------------------------
                # ERRORES DE ESCRITURA
                # --------------------------------------------------

                "que tecnolojia maneja",
                "que tecnolojias maneja",
                "que tecnolojia manejas",
                "que tecnolojias manejas",

                "que tecnoligia maneja",
                "que tecnoligias maneja",
                "que tecnoligia manejas",
                "que tecnoligias manejas",

                "que tecnlogia maneja",
                "que tecnlogias maneja",
                "que tecnlogia manejas",
                "que tecnlogias manejas",

                "que tecnolgia maneja",
                "que tecnolgia manejas",

                "que tegnologia maneja",
                "que tegnologias maneja",
                "que tegnologia manejas",
                "que tegnologias manejas",

                "que tecnologias manaja",
                "que tecnologias manajas",

                "que tecnoligias manaja",
                "que tecnoligias manajas",

                "que lenguajes manaja",
                "que lenguajes manajas",

                "que sabe aser",
                "que sabes aser",

                "que puede aser",
                "que puedes aser",

                "que erramientas maneja",
                "que erramientas manejas",
            ],

            # ======================================================
            # CERTIFICATIONS
            # ======================================================

            ChatIntent.CERTIFICATION: [
                "certificacion",
                "certificaciones",
                "certificasion",
                "certificasiones",
                "certificacioness",

                "certificado",
                "certificados",

                "curso",
                "cursos",

                "diploma",
                "diplomas",

                "constancia",
                "constancias",

                "acreditacion",

                "freecodecamp",
                "free code camp",

                "cisco",
                "cisco networking",

                "kaggle",

                "que certificaciones tienes",
                "tus certificaciones",

                "que cursos tienes",
                "tus cursos",
            ],

            # ======================================================
            # GITHUB
            # ======================================================

            ChatIntent.GITHUB: [
                "github",
                "git hub",
                "gitnub",
                "githup",
                "githib",
                "gitthub",

                "perfil github",
                "perfil de github",
                "perfil en github",

                "github profile",
                "mi github",
                "tu github",

                "repositorio",
                "repositorios",
                "repositorioos",
                "repos",
                "repo",

                "repositorio de github",
                "repositorios de github",

                "codigo",
                "codigo fuente",
                "source code",

                "commit",
                "commits",
                "comit",
                "comits",

                "contribucion",
                "contribuciones",
                "contribution",
                "contributions",

                "actividad de github",
                "actividad en github",

                "proyectos de github",
                "proyectos en github",

                "usuario de github",
                "username de github",

                "cuenta de github",

                "link de github",
                "enlace de github",
                "url de github",

                "github url",
                "github link",

                "git",
            ],
        }

        # ==========================================================
        # PALABRAS ESPECÍFICAS
        # ==========================================================

        self.specific_keywords = {

            # ------------------------------------------------------
            # SKILLS
            # ------------------------------------------------------

            "react": ChatIntent.SKILL,
            "angular": ChatIntent.SKILL,
            "flutter": ChatIntent.SKILL,
            "python": ChatIntent.SKILL,
            "fastapi": ChatIntent.SKILL,
            "flask": ChatIntent.SKILL,
            "typescript": ChatIntent.SKILL,
            "javascript": ChatIntent.SKILL,
            "tailwind": ChatIntent.SKILL,
            "html": ChatIntent.SKILL,
            "css": ChatIntent.SKILL,
            "postgresql": ChatIntent.SKILL,
            "postgres": ChatIntent.SKILL,
            "mysql": ChatIntent.SKILL,
            "sql": ChatIntent.SKILL,
            "sql server": ChatIntent.SKILL,
            "dart": ChatIntent.SKILL,
            "arduino": ChatIntent.SKILL,
            "esp32": ChatIntent.SKILL,
            "micropython": ChatIntent.SKILL,
            "gemini": ChatIntent.SKILL,
            "postman": ChatIntent.SKILL,
            "vercel": ChatIntent.SKILL,
            "render": ChatIntent.SKILL,
            "visual studio": ChatIntent.SKILL,
            "vscode": ChatIntent.SKILL,

            # ------------------------------------------------------
            # GITHUB
            # ------------------------------------------------------

            "github": ChatIntent.GITHUB,
            "git hub": ChatIntent.GITHUB,
            "githup": ChatIntent.GITHUB,
            "gitnub": ChatIntent.GITHUB,

            "repositorio": ChatIntent.GITHUB,
            "repositorios": ChatIntent.GITHUB,
            "repos": ChatIntent.GITHUB,
            "repo": ChatIntent.GITHUB,

            "commit": ChatIntent.GITHUB,
            "commits": ChatIntent.GITHUB,
            "comit": ChatIntent.GITHUB,

            "contribucion": ChatIntent.GITHUB,
            "contribuciones": ChatIntent.GITHUB,
            "contribution": ChatIntent.GITHUB,
            "contributions": ChatIntent.GITHUB,

            # ------------------------------------------------------
            # PROFILE
            # ------------------------------------------------------

            "perfil": ChatIntent.PROFILE,
            "curriculum": ChatIntent.PROFILE,
            "cv": ChatIntent.PROFILE,
            "presentate": ChatIntent.PROFILE,

            # ------------------------------------------------------
            # EXPERIENCE
            # ------------------------------------------------------

            "plenumsoft": ChatIntent.EXPERIENCE,

            # ------------------------------------------------------
            # EDUCATION
            # ------------------------------------------------------

            "itescam": ChatIntent.EDUCATION,

            # ------------------------------------------------------
            # CERTIFICATIONS
            # ------------------------------------------------------

            "freecodecamp": ChatIntent.CERTIFICATION,
            "cisco": ChatIntent.CERTIFICATION,
            "kaggle": ChatIntent.CERTIFICATION,
        }

    # ==========================================================
    # NORMALIZAR TEXTO
    # ==========================================================

    def normalize(self, text: str) -> str:

        text = text.lower().strip()

        text = unicodedata.normalize(
            "NFD",
            text
        )

        text = "".join(
            char
            for char in text
            if unicodedata.category(char) != "Mn"
        )

        return text

    # ==========================================================
    # DETECTAR INTENCIÓN
    # ==========================================================

    def detect(self, question: str) -> ChatIntent:

        question = self.normalize(question)

        scores = {}

        # ------------------------------------------------------
        # Calcular puntuación de cada intención
        # ------------------------------------------------------

        for intent, keywords in self.intents.items():

            score = 0

            for keyword in keywords:

                normalized_keyword = self.normalize(keyword)

                if normalized_keyword in question:

                    # Las frases tienen mayor peso
                    # que las palabras individuales.

                    if len(normalized_keyword.split()) > 1:
                        score += 2
                    else:
                        score += 1

            scores[intent] = score

        # ------------------------------------------------------
        # Obtener la puntuación máxima
        # ------------------------------------------------------

        max_score = max(scores.values())

        # ------------------------------------------------------
        # No se encontró ninguna coincidencia
        # ------------------------------------------------------

        if max_score == 0:

            return ChatIntent.UNKNOWN

        # ------------------------------------------------------
        # Obtener los intents con mayor puntuación
        # ------------------------------------------------------

        best_intents = [
            intent
            for intent, score in scores.items()
            if score == max_score
        ]

        # ------------------------------------------------------
        # Resolver empates
        # ------------------------------------------------------

        if len(best_intents) > 1:

            for word, intent in self.specific_keywords.items():

                normalized_word = self.normalize(word)

                if (
                    normalized_word in question
                    and intent in best_intents
                ):

                    return intent

        # ------------------------------------------------------
        # Palabras específicas
        #
        # Ejemplo:
        #
        # "¿Qué sabes de React?"
        #
        # Aunque la pregunta no diga "tecnología",
        # React determina que se trata de SKILL.
        # ------------------------------------------------------

        for word, specific_intent in self.specific_keywords.items():

            normalized_word = self.normalize(word)

            if normalized_word not in question:
                continue

            # GitHub explícito tiene prioridad.
            if specific_intent == ChatIntent.GITHUB:

                return ChatIntent.GITHUB

            # Una tecnología concreta solamente debe
            # convertir la pregunta en SKILL cuando
            # SKILL ya sea una de las intenciones detectadas
            # o cuando no exista otra intención clara.

            if specific_intent == ChatIntent.SKILL:

                if ChatIntent.SKILL in best_intents:

                    return ChatIntent.SKILL

        # ------------------------------------------------------
        # Resultado final
        # ------------------------------------------------------

        return best_intents[0]