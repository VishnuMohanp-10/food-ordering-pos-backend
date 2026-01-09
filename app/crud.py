from sqlalchemy.orm import Session
from .import models, schemas
from app import models, schemas
from app.audit import log_change

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_variant(db: Session, variant: schemas.VariantCreate):
    db_variant = models.Variant(**variant.dict())
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant

def update_item(db: Session, item_id:int, item_data:schemas.ItemUpdate):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not item:
        return None

    for field, value in item_data.dict(exclude_unset=True).items():
        
        old_value = getattr(item, field)
        if old_value != value:
            setattr(item,field, value)
            log_change(db=db, user="admin",entity_type="Item",entity_id = item.id,field_name = field, old_value=old_value,new_value= value,)
    
    db.commit()
    db.refresh(item)
    return item

def  update_variant(db:Session,variant_id:int, variant_data:schemas.VariantUpdate):
    variant=(
        db.query(models.Variant).filter(models.Variant.id == variant_id) .first()

    )
    if not variant:
        return None
    for field, value in variant_data.dict(exclude_unset=True).items():
        old_value = getattr(variant, field)
        if old_value != value:
            setattr(variant, field, value)
            log_change(db=db, user="admin", entity_type="Variant", entity_id=Variant.id, field_name=field, old_value= old_value, new_value= value,)

    
    db.commit()
    db.refresh(variant)
    return variant

 