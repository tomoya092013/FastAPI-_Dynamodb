from typing import List
from fastapi import APIRouter
from app.db.database import dynamodb
from app.models.careUser import CareUser
from app.services.careUser_service import CareUserService

routes_care_user = APIRouter()
careUsers_table = dynamodb().Table("careUser")

@routes_care_user.post("/care_users/")
def create_care_user(care_user: CareUser):
    CareUserService.create_care_user(care_user)
    return {"message": f"介護者 '{care_user.id}' を作成しました。"}

@routes_care_user.get("/care_users/", response_model=List[CareUser])
def get_all_care_users():
    care_users: List[CareUser] = CareUserService.get_all_care_users()
    return care_users

@routes_care_user.get("/care_users/{user_id}", response_model=List[CareUser])
def get_care_users(user_id: str):
    care_users: List[CareUser] = CareUserService.get_care_users_by_user_id(user_id=user_id)
    return care_users
