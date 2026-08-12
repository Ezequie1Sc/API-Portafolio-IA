import json
from pathlib import Path

from app.services.knowledge.project_service import ProjectService
from app.services.knowledge.certification_service import CertificationService


class KnowledgeService:

    def __init__(self):

        self.base_path = Path(__file__).parent.parent / "data"

        self.project_service = ProjectService()
        self.certification_service = CertificationService()

    # =====================================
    # Método interno
    # =====================================

    def _load_json(self, path: Path):

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    # =====================================
    # Información general
    # =====================================

    def get_profile(self):

        return self._load_json(
            self.base_path / "profile.json"
        )

    def get_contact(self):

        return self._load_json(
            self.base_path / "contact.json"
        )

    def get_education(self):

        return self._load_json(
            self.base_path / "education.json"
        )

    def get_experience(self):

        return self._load_json(
            self.base_path / "experience.json"
        )

    def get_personality(self):

        return self._load_json(
            self.base_path / "personality.json"
        )

    def get_metadata(self):

        return self._load_json(
            self.base_path / "metadata.json"
        )

    # =====================================
    # Skills
    # =====================================

    def get_skills_index(self):

        return self._load_json(
            self.base_path / "skills" / "index.json"
        )

    def get_skill(self, filename: str):

        return self._load_json(
            self.base_path / "skills" / filename
        )

    # =====================================
    # Certificaciones
    # =====================================

    def get_certifications(self):

        return self.certification_service.get()

    # =====================================
    # Contexto Base
    # =====================================

    def get_base_context(self):

        return {

            "profile": self.get_profile(),

            "contact": self.get_contact(),

            "education": self.get_education(),

            "experience": self.get_experience(),

            "personality": self.get_personality(),

            "metadata": self.get_metadata()

        }

    # =====================================
    # Construcción del contexto
    # =====================================

    def search(self, question: str):

        question = question.lower().strip()

        context = self.get_base_context()

        # =====================================
        # PROYECTOS
        # =====================================

        try:

            projects = self.project_service.search(question)

            print("\n========== PROYECTOS ==========")
            print("Pregunta:", question)
            print("Proyectos encontrados:", len(projects))
            print(projects)
            print("===============================\n")

            if projects:

                context["projects"] = projects

        except Exception as e:

            print("\nERROR EN PROJECTSERVICE")
            print(e)
            print()

        # =====================================
        # SKILLS
        # =====================================

        try:

            skills = []

            skills_index = self.get_skills_index()

            for skill in skills_index["skills"]:

                keywords = [
                    keyword.lower()
                    for keyword in skill["keywords"]
                ]

                if any(
                    keyword in question
                    for keyword in keywords
                ):

                    skills.append(
                        self.get_skill(skill["file"])
                    )

            if skills:

                context["skills"] = skills

        except Exception as e:

            print("\nERROR EN SKILLS")
            print(e)
            print()

        # =====================================
        # CERTIFICACIONES
        # =====================================

        try:

            certification_keywords = [
                "certificación",
                "certificaciones",
                "certificado",
                "certificados",
                "curso",
                "cursos",
                "credencial",
                "credenciales",
                "freecodecamp",
                "microsoft",
                "cisco",
                "kaggle",
                "anthropic",
                "linkedin learning"
            ]

            if any(
                keyword in question
                for keyword in certification_keywords
            ):

                certifications = self.certification_service.search(
                    question
                )

                if certifications:

                    context["certifications"] = certifications

        except Exception as e:

            print("\nERROR EN CERTIFICACIONES")
            print(e)
            print()

        # =====================================
        # CONTEXTO FINAL
        # =====================================

        print("\n========== CONTEXTO FINAL ==========")
        print(context.keys())
        print("====================================\n")

        return context