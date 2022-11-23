from pydantic import BaseModel

class SCHEMAAPPKEY(BaseModel):
    app_key: str

class SCHEMALOCATIONS(BaseModel):
    id: int
    country: str
    city: str
    state: str
    latitude: str
    longitude: str