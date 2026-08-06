from app.services.knowledge.base_data_service import BaseDataService


class SkillService(BaseDataService):

    def __init__(self):

        super().__init__()

    def get(self):

        return self.load_json("skills.json")

    def search(self, question: str):

        question = question.lower()

        skills = self.get()

        matches = []

        for category, technologies in skills.items():

            if isinstance(technologies, list):

                for tech in technologies:

                    if question in tech.lower() or tech.lower() in question:

                        matches.append(tech)

        if matches:

            return {
                "matches": matches,
                "skills": skills
            }

        return skills