from sqlalchemy.orm import Session
from app.domain.models.order import Order
from app.schemas.order_schema import OrderCreate, OrderUpdate
from app.infrastructure.db.cache import get_cache, set_cache  
from app.infrastructure.db.database import get_db


class OrderRepository:
    @staticmethod
    def create_order(db: Session, order_data: OrderCreate, user_id: int):
        new_order = Order(
            customer_name=order_data.customer_name,
            status="pending",
            total_price=order_data.total_price,
            user_id=user_id
        )
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        set_cache("orders_list", None)

        return new_order.to_dict() 

    @staticmethod
    def get_orders(db: Session, status: str = None, min_price: float = None, max_price: float = None):
        cache_key = f"orders_list_{status}_{min_price}_{max_price}"
        cached_orders = get_cache(cache_key)

        if cached_orders:
            return cached_orders  

        query = db.query(Order)
        if status:
            query = query.filter(Order.status == status)
        if min_price:
            query = query.filter(Order.total_price >= min_price)
        if max_price:
            query = query.filter(Order.total_price <= max_price)

        orders = query.all()
        orders_list = [order.to_dict() for order in orders]  

        set_cache(cache_key, orders_list, timeout=120) 

        return orders_list

    @staticmethod
    def get_order_by_id(db: Session, order_id: int):
        cache_key = f"order_{order_id}"
        cached_order = get_cache(cache_key)

        if cached_order:
            return cached_order  

        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            order_dict = order.to_dict()
            set_cache(cache_key, order_dict, timeout=120)  
            return order_dict

        return None

    @staticmethod
    def update_order(db: Session, order_id: int, order_data: OrderUpdate):
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            order.customer_name = order_data.customer_name
            order.status = order_data.status
            order.total_price = order_data.total_price
            db.commit()
            db.refresh(order)

            order_dict = order.to_dict()

            set_cache(f"order_{order_id}", order_dict)
            set_cache("orders_list", None)  

            return order_dict

        return None

    @staticmethod
    def soft_delete_order(db: Session, order_id: int):
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            order.status = "cancelled"
            db.commit()
            db.refresh(order)

            set_cache(f"order_{order_id}", None)
            set_cache("orders_list", None) 

            return order.to_dict()

        return None
