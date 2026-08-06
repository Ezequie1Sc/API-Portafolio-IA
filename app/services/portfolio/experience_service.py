from app.services.portfolio.base_data_service import BaseDataService


class ExperienceService(BaseDataService):

    def __init__(self):

        super().__init__()

    def get(self):

        return self.load_json("experience.json")