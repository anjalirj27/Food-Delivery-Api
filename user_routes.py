from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from fastapi_jwt_auth import AuthJWT

user_router = APIRouter(prefix="/user", tags=["users"])

@user_router.get("/profile")
def user_profile(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    user = db.query(User).filter(User.username == current_user).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff
    }
