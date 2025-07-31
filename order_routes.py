# order_routes.py
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from schemas import OrderModel
from database import SessionLocal
from models import Order
from recommendation import recommend_pizza
from predictor import predict_preparation_time

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/recommend")
def get_pizza_recommendation(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    pizza = recommend_pizza(int(user_id))
    return {"recommended_pizza": pizza}

@order_router.post("/place")
def place_order(order: OrderModel, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    
    prep_time = predict_preparation_time(order.pizza_type, order.quantity)

    db = SessionLocal()
    new_order = Order(
        user_id=user_id,
        pizza_type=order.pizza_type,
        quantity=order.quantity,
        status="Preparing"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()

    return {
        "message": "Order placed successfully",
        "order_id": new_order.id,
        "estimated_preparation_time": f"{prep_time} minutes"
    }
