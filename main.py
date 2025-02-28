from fastapi import FastAPI
from mangum import Mangum
from app.routes.user_routes import routes_user
from app.routes.careUser_routes import routes_care_user

app = FastAPI()

@app.get("/")
def read_root():
    return {"こんにちは, FastAPI"}

app.include_router(routes_user)
app.include_router(routes_care_user)

handler = Mangum(app)
