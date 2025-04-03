from fastapi import APIRouter, Depends, HTTPException
from models.product_model import ProductModel
from schema.product_schema import ProductSchema


router=APIRouter()

@router.post("/add")
def add_product(product:ProductSchema):
    product_data = product.dict()
    product_id= ProductModel.create_product(product_data)
    return {"message": "Product added successfully", "product_id": product_id}


@router.get("/{product_id}")
def get_product(product_id:str):
    product=ProductModel.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
