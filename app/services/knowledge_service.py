import json
from pathlib import Path


class KnowledgeService:

    def __init__(self):

        self.base_path = Path(__file__).parent.parent / "data"

    def _load_json(self, filename: str):

        file_path = self.base_path / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_context(self):

        knowledge = {

            "profile": self._load_json("profile.json"),

            "projects": self._load_json("projects.json"),

            "skills": self._load_json("skills.json"),

            "experience": self._load_json("experience.json")
        }

        return knowledge