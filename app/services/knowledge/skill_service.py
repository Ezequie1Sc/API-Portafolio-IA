from app.services.knowledge.base_data_service import BaseDataService


class SkillService(BaseDataService):

    def __init__(self):

        super().__init__()

    def get(self):

        return self.load_json("skills.json")

    def search(self, question: str):

        question = question.lower()

        skills = self.get()

        result = {}

        for category, content in skills.items():

            if not isinstance(content, dict):
                continue

            technologies = content.get("technologies", [])

            matches = []

            for tech in technologies:

                name = tech.get("name", "").lower()

                if (
                    name in question
                    or question in name
                ):
                    matches.append(tech)

            if matches:

                result[category] = {

                    "description": content.get("description", ""),

                    "technologies": matches

                }

        # Si encontró tecnologías específicas
        if result:

            return result

        # Si preguntan "¿Qué tecnologías maneja?"
        if any(
            word in question
            for word in [
                "tecnologias",
                "tecnología",
                "tecnologia",
                "stack",
                "habilidades",
                "skills"
            ]
        ):

            return skills

        return {}