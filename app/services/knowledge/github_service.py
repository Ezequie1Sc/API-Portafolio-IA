import requests

from app.services.knowledge.base_data_service import BaseDataService


class GithubService(BaseDataService):

    def __init__(self):

        super().__init__()

    def get(self):

        config = self.load_json("github.json")

        username = config["username"]

        response = requests.get(
            f"https://api.github.com/users/{username}",
            timeout=10
        )

        response.raise_for_status()

        github = response.json()

        return {

            "name": github.get("name"),

            "username": github.get("login"),

            "avatar": github.get("avatar_url"),

            "bio": github.get("bio"),

            "profile_url": github.get("html_url"),

            "repositories_url":
                github.get("html_url") + "?tab=repositories",

            "public_repositories":
                github.get("public_repos"),

            "contributions_chart":
                f"https://ghchart.rshah.org/2563eb/{github.get('login')}"

        }