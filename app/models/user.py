from pydantic import BaseModel

class User(BaseModel):
	id: str
	name: str
	password: str
	email: str
	phoneNumber: str
	facilityName: str
	facilityPhoneNumber: str
	facilityAddress: str
