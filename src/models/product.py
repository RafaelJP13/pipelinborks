from sqlalchemy import Column, Integer, String
from src.db import Base

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_name = Column(String(255), nullable=False)
    product_name = Column(String(255), nullable=False)
    ingredient_name = Column(String(255), nullable=False)
    ingredient_strength = Column(String(50), nullable=False)


