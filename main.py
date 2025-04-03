from fastapi import FastAPI
from configurations import db
from routes.user_routes import router as user_router
app= FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")


async def root():
   try:
      db.command("ping")
      return {"message": "MongoDB is connected"}
   except Exception as e:
        return {"message": "MongoDB is not connected", "error": str(e)}
       