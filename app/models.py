from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime , JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Item(Base):
    __tablename__ = "items"
     

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    category = Column(String, nullable=False)
    product_code = Column(String, unique=True, nullable=False)
    branch_id = Column(Integer, nullable=False)
     
    variants = relationship("Variant", back_populates="item")

class Variant(Base):
    __tablename__ = "variants"
  
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    variant_name = Column(String, nullable=False)
    selling_price = Column(Float, nullable=False)
    cost_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    properties = Column(JSON , default={})

    item = relationship("Item", back_populates="variants")

class AuditLog(Base):
    __tablename__ = "audit_logs"
  
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    entity_type = Column(String, nullable= False)
    entity_id = Column(Integer, nullable=False)
    field_name = Column(String, nullable=False)
    old_value = Column(String)
    new_value = Column(String)
    timestamp = Column(DateTime, default= datetime.utcnow)

