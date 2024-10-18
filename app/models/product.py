from sqlalchemy import *
from app.db import Base

class Product(Base):
    __tablename__ = "Product"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR)
    price = Column(DECIMAL)