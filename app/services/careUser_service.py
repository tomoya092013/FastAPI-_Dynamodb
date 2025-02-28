from app.db.database import dynamodb
from app.models.careUser import CareUser
from boto3.dynamodb.conditions import Key

care_users_table = dynamodb().Table("careUsers")

class CareUserService:
	@staticmethod
	def create_care_user(careUser: CareUser):
		care_users_table.put_item(Item=careUser.model_dump())

	@staticmethod
	def get_all_care_users():
		response = care_users_table.scan()
		return response.get("Items", [])
    
	@staticmethod
	def get_care_users_by_user_id(user_id: str):
		response = care_users_table.query(
			IndexName="GSIuserId",
			KeyConditionExpression=Key("userId").eq(user_id)
		)
		return response.get("Items", [])
