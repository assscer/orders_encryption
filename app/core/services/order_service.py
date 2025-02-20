from sqlalchemy.orm import Session
from app.infrastructure.db.repository.order_repository import OrderRepository
from app.schemas.order_schema import OrderCreate, OrderUpdate

class OrderService:
    @staticmethod
    def create_order(db: Session, order_data: OrderCreate, user_id: int):
        return OrderRepository.create_order(db, order_data, user_id)

    @staticmethod
    def get_orders(db: Session, status: str = None, min_price: float = None, max_price: float = None):
        return OrderRepository.get_orders(db, status, min_price, max_price)

    @staticmethod
    def get_order_by_id(db: Session, order_id: int):
        return OrderRepository.get_order_by_id(db, order_id)

    @staticmethod
    def update_order(db: Session, order_id: int, order_data: OrderUpdate):
        return OrderRepository.update_order(db, order_id, order_data)

    @staticmethod
    def soft_delete_order(db: Session, order_id: int):
        return OrderRepository.soft_delete_order(db, order_id)
