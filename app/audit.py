from sqlalchemy.orm import Session
from app.models import AuditLog


def log_change(
    db:Session,
    user: str,
    entity_type:str,
    entity_id:int,
    field_name:str,
    old_value,
    new_value
):
    audit = AuditLog(
        user = user,
        entity_type=entity_type,
        entity_id=entity_id,
        field_name=field_name,
        old_value = str(old_value),
        new_value=str(new_value),

    )
    db.add(audit)
    db.commit()