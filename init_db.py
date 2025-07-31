from database import engine, Base
from models import User,Order

Base.metadata.create_all(bind = engine)
#print("tables created successfully in pizza_delivery.db")
