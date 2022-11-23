from sqlalchemy.orm import Session
import models, schemas
from location import Location

def create_app_key(db: Session, app_key: str ):
    db_app_key = models.TABLEAPPKEY(appkey = app_key)    
    db.add(db_app_key)
    db.commit()
    db.refresh(db_app_key)
    
def create_locations(db: Session, loc: Location ):
    db_location = models.TABLELOCATION(country = loc.country, city = loc.city, state = loc.state, latitude = loc.latitude, longitude = loc.longitude)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    
def get_locations_by_address(db: Session, loc: Location) -> models.TABLELOCATION:
    db_location = db.query(models.TABLELOCATION).filter(models.TABLELOCATION.city == loc.city, models.TABLELOCATION.state == loc.state, models.TABLELOCATION.country == loc.country).first()
    return db_location

def get_app_key_by_id(db: Session, id: int) -> models.TABLEAPPKEY:
    db_app_key = db.query(models.TABLEAPPKEY).filter(models.TABLEAPPKEY.id == id).first()
    return db_app_key