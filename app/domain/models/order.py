from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending") 
    total_price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))  

    products = relationship("Product", backref="order", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "status": self.status,
            "total_price": self.total_price,
            "user_id": self.user_id,
            "products": [product.to_dict() for product in self.products] if self.products else []
        }
