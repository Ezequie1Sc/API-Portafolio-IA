from app.services.knowledge.base_data_service import BaseDataService


class CertificationService(BaseDataService):

    def __init__(self):

        super().__init__()

    def get(self):

        return self.load_json("certifications.json")

    def search(self, question: str):

        return self.get()