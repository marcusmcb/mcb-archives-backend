from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class RadioShowBase(BaseModel):
    title: str
    description: Optional[str] = None
    image: Optional[str] = None
    original_broadcast_date: Optional[date] = None
    file_url: Optional[str] = None
    playlist: Optional[str] = None
    show_type: Optional[str] = None

class RadioShowCreate(RadioShowBase):
    pass

class RadioShowOut(RadioShowBase):
    id: int
    date_added: datetime

    class Config:
        orm_mode = True
