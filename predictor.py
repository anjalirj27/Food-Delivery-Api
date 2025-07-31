# predictor.py
import random

def predict_preparation_time(pizza_type: str, quantity: int) -> int:
    base_time = {
        "Margherita": 10,
        "Pepperoni": 12,
        "Hawaiian": 14,
        "Farmhouse": 15
    }
    return base_time.get(pizza_type, 12) + quantity * random.randint(2, 5)
