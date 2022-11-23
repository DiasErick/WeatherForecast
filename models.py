from sqlalchemy import Boolean, Column, Integer, String

from database import Base

class TABLEAPPKEY(Base):
    __tablename__ = "appkey"
    id = Column(Integer, primary_key=True)
    appkey = Column(String, index=True)
    
class TABLELOCATION(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key = True)
    country = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    latitude = Column(String )
    longitude = Column(String)
    
    