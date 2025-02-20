import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app_logs.log"),  
        logging.StreamHandler()  
    ]
)

logger = logging.getLogger(__name__)

def log_order_creation(order_id: int):
    logger.info(f"Order {order_id} created.")

def log_order_update(order_id: int):
    logger.info(f"Order {order_id} updated.")

def log_order_deletion(order_id: int):
    logger.info(f"Order {order_id} soft deleted.")
