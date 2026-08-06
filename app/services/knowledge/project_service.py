import json
from pathlib import Path


class ProjectService:

    def __init__(self):

        self.projects_path = (
            Path(__file__).parent.parent.parent
            / "data"
            / "projects"
        )

        self.index = self._load_json("index.json")

    # ===================================================
    # Utilidades
    # ===================================================

    def _load_json(self, filename: str):

        file_path = self.projects_path / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    # ===================================================
    # Buscar proyectos
    # ===================================================

    def search(self, question: str):

        question = question.lower().strip()

        candidates = []

        for item in self.index["projects"]:

            score = 0

            if item["name"].lower() in question:
                score += 10

            if item["id"].lower() in question:
                score += 10

            if item.get("category", "").lower() in question:
                score += 3

            for keyword in item.get("keywords", []):

                if keyword.lower() in question:
                    score += 2

            if item.get("featured", False):

                if any(
                    word in question
                    for word in [
                        "importante",
                        "importantes",
                        "principal",
                        "principales",
                        "mejor",
                        "mejores",
                        "destacado",
                        "destacados",
                    ]
                ):
                    score += 5

            if score > 0:

                candidates.append(
                    {
                        "file": item["file"],
                        "score": score,
                    }
                )

        candidates.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        files = []
        used = set()

        for candidate in candidates:

            if candidate["file"] in used:
                continue

            used.add(candidate["file"])
            files.append(candidate["file"])

        projects = []

        for filename in files:

            try:

                projects.append(
                    self._load_json(filename)
                )

            except Exception as e:

                print(f"Error cargando {filename}: {e}")

        print("\n========== PROJECT SERVICE ==========")
        print("Pregunta:", question)
        print("Archivos encontrados:", files)
        print("=====================================\n")

        return projects