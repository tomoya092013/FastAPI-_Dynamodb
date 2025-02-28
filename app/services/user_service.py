from app.db.database import dynamodb
from app.models.user import User

users_table = dynamodb().Table("users")

class UserService:
    @staticmethod
    def create_user(user: User):
        users_table.put_item(Item=user.model_dump())

    @staticmethod
    def get_all_users():
        response = users_table.scan()
        return response.get("Items", [])
