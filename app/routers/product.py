from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import select, asc, desc, func
from app.db import get_db
from app.models.product import Product

router = APIRouter()

@router.get("/products")
def index(request: Request, start: int, length: int = 10, db: Session = Depends(get_db)):
    params = request.query_params.get
    order = "id"
    if params("order[0][column]"):
        order = params("columns[" + params("order[0][column]") + "][data]")
    direction = params("order[0][dir]", "asc")
    sort_direction = asc if direction == "asc" else desc
    query = db.query(Product)
    recordsTotal = query.count()
    search = params("search[value]")
    if search:
        query = query.filter(Product.name.like(f"%{search}%"))
    recordsFiltered = query.count()
    products = (
        query
        .order_by(sort_direction(getattr(Product, order)))
        .offset(start)
        .limit(length)
        .all()
    )
    return {
        "draw": params("draw"),
        "recordsTotal": recordsTotal,
        "recordsFiltered": recordsFiltered,
        "data": products
    }