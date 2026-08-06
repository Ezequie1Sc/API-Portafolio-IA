from app.services.knowledge.base_data_service import BaseDataService


class MetadataService(BaseDataService):

    def __init__(self):
        super().__init__()

    def get(self):
        return self.load_json("metadata.json")