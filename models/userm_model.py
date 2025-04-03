from bson import ObjectId
from configurations import user_collection

class UserModel:
    @staticmethod
    def create_user(user_data: dict):
        """Insert a new user into MongoDB."""
        user_data["_id"] = ObjectId()  # Assign unique ObjectId
        result = user_collection.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def get_user_by_email(email: str):
        """Retrieve a user by email."""
        user = user_collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user

    @staticmethod
    def get_user_by_id(user_id: str):
        """Retrieve a user by ID."""
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["_id"] = str(user["_id"])
        return user



