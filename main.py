from fastapi import FastAPI
from configurations import db
app= FastAPI()

@app.get("/")

async def root():
   try:
      db.command("ping")
      return {"message": "MongoDB is connected"}
   except Exception as e:
        return {"message": "MongoDB is not connected", "error": str(e)}
       