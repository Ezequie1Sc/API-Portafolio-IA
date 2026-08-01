import json
from pathlib import Path


class ProjectService:

    def __init__(self):

        self.projects_path = (
            Path(__file__).parent.parent /
            "data" /
            "projects"
        )

        self.index = self._load_json("index.json")

    # ===================================================
    # Utilidades
    # ===================================================

    def _load_json(self, filename: str):

        file_path = self.projects_path / filename

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    def _all_projects(self):

        projects = []

        for item in self.index["projects"]:

            try:

                projects.append(
                    self._load_json(item["file"])
                )

            except Exception:

                pass

        return projects

    # ===================================================
    # Búsquedas
    # ===================================================

    def search_by_name(self, question: str):

        question = question.lower()

        results = []

        for project in self._all_projects():

            if project["name"].lower() in question:

                results.append(project)

        return results

    def search_by_keywords(self, question: str):

        question = question.lower()

        results = []

        for project in self._all_projects():

            recruiter = project.get("recruiter", {})

            keywords = recruiter.get("keywords", [])

            keywords = [
                keyword.lower()
                for keyword in keywords
            ]

            if any(keyword in question for keyword in keywords):

                results.append(project)

        return results

    def search_by_technology(self, question: str):

        question = question.lower()

        results = []

        for project in self._all_projects():

            technologies = [

                tech.lower()

                for tech in project.get(
                    "technologies",
                    []
                )

            ]

            if any(
                tech in question
                for tech in technologies
            ):

                results.append(project)

        return results

    def search_by_category(self, question: str):

        question = question.lower()

        results = []

        for project in self._all_projects():

            category = project.get(
                "category",
                ""
            ).lower()

            if category in question:

                results.append(project)

        return results

    def search_by_type(self, question: str):

        question = question.lower()

        results = []

        for project in self._all_projects():

            project_type = project.get(
                "type",
                ""
            ).lower()

            if project_type in question:

                results.append(project)

        return results

    def search_featured(self):

        results = []

        for project in self._all_projects():

            if project.get(
                "featured",
                False
            ):

                results.append(project)

        return results

    def search_production(self):

        results = []

        for project in self._all_projects():

            if project.get(
                "production_ready",
                False
            ):

                results.append(project)

        return results

    def search_difficulty(self, level):

        results = []

        for project in self._all_projects():

            difficulty = project.get(
                "difficulty",
                {}
            ).get(
                "overall",
                ""
            )

            if difficulty.lower() == level.lower():

                results.append(project)

        return results

    # ===================================================
    # Motor inteligente
    # ===================================================

    def search(self, question: str):

        question = question.lower()

        context = []

        # -----------------------------
        # Nombre
        # -----------------------------

        context.extend(
            self.search_by_name(question)
        )

        # -----------------------------
        # Keywords
        # -----------------------------

        context.extend(
            self.search_by_keywords(question)
        )

        # -----------------------------
        # Tecnologías
        # -----------------------------

        context.extend(
            self.search_by_technology(question)
        )

        # -----------------------------
        # Categorías
        # -----------------------------

        context.extend(
            self.search_by_category(question)
        )

        # -----------------------------
        # Tipo
        # -----------------------------

        context.extend(
            self.search_by_type(question)
        )

        # -----------------------------
        # Destacados
        # -----------------------------

        if (

            "importante" in question

            or

            "mejor" in question

            or

            "destacado" in question

            or

            "principal" in question

        ):

            context.extend(
                self.search_featured()
            )

        # -----------------------------
        # Producción
        # -----------------------------

        if (

            "producción" in question

            or

            "production" in question

        ):

            context.extend(
                self.search_production()
            )

        # -----------------------------
        # Complejidad
        # -----------------------------

        if (

            "difícil" in question

            or

            "complejo" in question

        ):

            context.extend(
                self.search_difficulty(
                    "Alta"
                )
            )

        # ===================================================
        # Eliminar duplicados
        # ===================================================

        unique = {}

        for project in context:

            unique[
                project["id"]
            ] = project

        return list(
            unique.values()
        )