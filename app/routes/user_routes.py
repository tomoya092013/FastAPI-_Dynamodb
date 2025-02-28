from fastapi import APIRouter
from app.db.database import dynamodb
from app.models.careUser import CareUser
from app.models.user import User
from typing import List
from app.services.user_service import UserService

routes_user = APIRouter()
users_table = dynamodb().Table("users")

@routes_user.post("/users/")
def create_user(user: User):
    UserService.create_user(user)
    return {"message": f"ユーザー '{user.id}' を作成しました。"}

@routes_user.get("/users/", response_model=List[User])
def get_all_users():
    users: List[User] = UserService.get_all_users()
    return users
