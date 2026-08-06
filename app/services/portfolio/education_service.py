from app.services.portfolio.base_data_service import BaseDataService


class EducationService(BaseDataService):

    def __init__(self):

        super().__init__()

    def get(self):

        return self.load_json("education.json")