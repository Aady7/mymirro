from fastapi import FastAPI
from configurations import db
from routes.user_routes import router as user_router
from routes.product_routes import router as product_router
app= FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(product_router, prefix="/products", tags=["Products"])

@app.get("/")


async def root():
   try:
      db.command("ping")
      return {"message": "MongoDB is connected"}
   except Exception as e:
        return {"message": "MongoDB is not connected", "error": str(e)}
       