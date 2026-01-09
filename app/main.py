from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models, schemas, crud


models.Base.metadata.create_all(bind = engine)

app = FastAPI(title="Food Ordering POS ")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()


@app.get("/")
def root():
    return {"message": "POS Backend is running"}

@app.post("/items")
def create_item(item: schemas.ItemCreate, db: Session= Depends(get_db)):
    return crud.create_item(db, item)

@app.post("/variants")
def create_variant(variant: schemas.VariantCreate, db:Session = Depends(get_db)):
    return crud.create_variant(db, variant)

@app.put("/items/{item_id}")
def update_item(
    item_id:int, 
    item: schemas.ItemUpdate,
    db: Session =  Depends(get_db), ):
    updated  = crud.update_item(db, item_id, item)
    if not updated :
        raise HTTPException(status_code=404,detail="Item not found")
    return updated

@app.put("/variants/{variant_id}")
def updated_variant(
    variant_id: int,
    variant:schemas.VariantUpdate,
    db: Session = Depends(get_db), ):

    updated =  crud.update_variant(db, variant_id, variant)
    if not updated:
       raise HTTPException(status_code=404, detail="Variant not found")
    return updated


@app.get("/audit-logs")
def get_audit_logs(db: Session =Depends(get_db)):
    return ( db.query(models.AuditLog).order_by(models.AuditLog.timestamp.desc()).all() )