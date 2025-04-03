from bson import ObjectId
from configurations import product_collection

class ProductModel:
    @staticmethod
    def create_product(product_data:dict):
        """Insert a new product into MongoDB."""
        product_data["_id"]=ObjectId()  
        result = product_collection.insert_one(product_data)
        return str(result.inserted_id)
    
    @staticmethod
    def get_product_by_id(product_id:str):
        product=product_collection.find_one({"_id":ObjectId(product_id)})
        if product:
            product["_id"]=str(product["_id"])
        return product
