import json
from pathlib import Path


class BaseDataService:

    def __init__(self):

        self.data_path = (
            Path(__file__).parent.parent.parent /
            "data"
        )

    def load_json(self, filename: str):

        file_path = self.data_path / filename

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)