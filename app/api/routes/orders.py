from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.services.order_service import OrderService
from app.infrastructure.db.base import SessionLocal
from app.schemas.order_schema import OrderCreate, OrderUpdate, OrderResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return OrderService.create_order(db, order, user_id=1) 

@router.get("/", response_model=list[OrderResponse])
def get_orders(status: str = None, min_price: float = None, max_price: float = None, db: Session = Depends(get_db)):
    return OrderService.get_orders(db, status, min_price, max_price)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = OrderService.get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    updated_order = OrderService.update_order(db, order_id, order)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}", response_model=OrderResponse)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    deleted_order = OrderService.soft_delete_order(db, order_id)
    if not deleted_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return deleted_order
