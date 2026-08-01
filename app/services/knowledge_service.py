import json
from pathlib import Path


class KnowledgeService:

    def __init__(self):
        self.base_path = Path(__file__).parent.parent / "data"

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
    # Índices
    # =====================================

    def get_projects_index(self):
        return self._load_json(
            self.base_path / "projects" / "index.json"
        )

    def get_skills_index(self):
        return self._load_json(
            self.base_path / "skills" / "index.json"
        )

    def get_certifications_index(self):
        return self._load_json(
            self.base_path / "certifications" / "index.json"
        )

    # =====================================
    # Archivos individuales
    # =====================================

    def get_project(self, filename: str):
        return self._load_json(
            self.base_path / "projects" / filename
        )

    def get_skill(self, filename: str):
        return self._load_json(
            self.base_path / "skills" / filename
        )

    def get_certification(self, filename: str):
        return self._load_json(
            self.base_path / "certifications" / filename
        )

    # =====================================
    # Contexto base
    # =====================================

    def get_base_context(self):

        return {
            "profile": self.get_profile(),
            "contact": self.get_contact(),
            "education": self.get_education(),
            "experience": self.get_experience(),
            "personality": self.get_personality()
        }

    # =====================================
    # Búsqueda inteligente
    # =====================================

    def search(self, question: str):

        question = question.lower()

        context = self.get_base_context()

        # -----------------------------
        # Buscar proyectos
        # -----------------------------

        try:

            projects = []

            projects_index = self.get_projects_index()

            for project in projects_index["projects"]:

                keywords = [
                    keyword.lower()
                    for keyword in project["keywords"]
                ]

                if any(keyword in question for keyword in keywords):

                    projects.append(
                        self.get_project(project["file"])
                    )

            if projects:
                context["projects"] = projects

        except Exception:
            pass

        # -----------------------------
        # Buscar habilidades
        # -----------------------------

        try:

            skills = []

            skills_index = self.get_skills_index()

            for skill in skills_index["skills"]:

                keywords = [
                    keyword.lower()
                    for keyword in skill["keywords"]
                ]

                if any(keyword in question for keyword in keywords):

                    skills.append(
                        self.get_skill(skill["file"])
                    )

            if skills:
                context["skills"] = skills

        except Exception:
            pass

        # -----------------------------
        # Buscar certificaciones
        # -----------------------------

        try:

            certifications = []

            cert_index = self.get_certifications_index()

            for cert in cert_index["certifications"]:

                keywords = [
                    keyword.lower()
                    for keyword in cert["keywords"]
                ]

                if any(keyword in question for keyword in keywords):

                    certifications.append(
                        self.get_certification(cert["file"])
                    )

            if certifications:
                context["certifications"] = certifications

        except Exception:
            pass

        return context