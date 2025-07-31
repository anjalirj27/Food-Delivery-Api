# recommendation.py
from collections import Counter
from database import SessionLocal
from models import Order

def recommend_pizza(user_id: int):
    db = SessionLocal()
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    db.close()

    if not orders:
        return "Margherita"  # default pizza

    pizza_names = [order.pizza_type for order in orders]
    most_common = Counter(pizza_names).most_common(1)[0][0]
    return most_common
