import logging
from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.product import productos
from schemas.product import Product
from typing import List

product = APIRouter()




@product.get("/product", response_model=List[Product], tags=["Products"])
def get_all_product():
    try:
        with conn.begin() as transaction:
            result = conn.execute(productos.select()).fetchall()
        return result or []  # Devuelve una lista vacía si result es None
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")







@product.post("/product", response_model=Product, tags=["Products"])
def create_product(product: Product):
    try:
        with conn.begin() as transaction:
            new_product= {
                "nombre_producto": product.name_product,
                "tipo_producto": product.type_product,
                "precio_producto": product.price_product,
            }
            result = conn.execute(product.insert().values(new_product))
            created_product = conn.execute(product.select().where(product.c.id == result.lastrowid)).first()
        return created_product
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")






@product.get("/product/{id}", response_model=Product, tags=["Products"])
def get_product(id: int):
    try:
        products = conn.execute(productos.select().where(productos.c.id_producto == id)).first()
        if products is not None:
            return products
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Products not found"
            )
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")





@product.put("/product/{id}", response_model=Product, tags=["Products"])
def update_product(id: int, product: Product):
    try:
        with conn.begin() as transaction:
            conn.execute(
                Product.update()
                .where(product.c.id == id)
                .values(
                    nombre_producto=product.name_product,
                    tipo_producto=product.type_product,
                    precio_producto=product.price_product,
                )
            )
            updated_product = conn.execute(productos.select().where(productos.c.id == id)).first()
        return updated_product
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")


@product.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT,
                                tags=["Products"])
def delete_product(id: int):
    try:
        with conn.begin() as transaction:
            deleted = conn.execute(productos.delete().where(productos.c.id == id))
            if deleted.rowcount == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Products not found"
                )
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")