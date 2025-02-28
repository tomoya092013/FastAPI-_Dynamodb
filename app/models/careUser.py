from pydantic import BaseModel

class CareUser(BaseModel):
	id: str
	userId: str
	name: str
	phoneNumber: str
	email: str
	familyName: str
	careLevel: str
	weight: int
	serviceType: str
	attendant: str
