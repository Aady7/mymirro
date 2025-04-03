from fastapi import APIRouter, Depends, HTTPException
from models.userm_model import UserModel
from schema.user_schema import UserSchema
from configurations import user_collection

router=APIRouter()

@router.post("/register")
def register_user(user:UserSchema):
    existing_user = UserModel.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_data = user.dict()
    user_id= UserModel.create_user(user_data)
    return {"message": "User registered successfully", "user_id": user_id}

@router.get("/user/{user_id}")
def  get_user(user_id:str):
    user=UserModel.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user