from fastapi import APIRouter

from app.services.knowledge.profile_service import ProfileService
from app.services.knowledge.skill_service import SkillService
from app.services.knowledge.github_service import GithubService


router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"]
)


profile_service = ProfileService()
skill_service = SkillService()
github_service = GithubService()


@router.get("/profile")
async def get_profile():
    return profile_service.get()


@router.get("/skills")
async def get_skills():
    return skill_service.get()


@router.get("/github")
async def get_github():
    return github_service.get()