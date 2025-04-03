from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class PreferencesSchema(BaseModel):
    style: List[str]
    color: List[str]
    size: Optional[str] = None

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str  # Hashed before storing
    preferences: PreferencesSchema
    created_at: datetime = datetime.utcnow()
