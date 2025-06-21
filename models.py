from sqlalchemy import Column, Integer, String, Date, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class RadioShow(Base):
    __tablename__ = "radio_shows"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    image = Column(String(255))  # URL or path to image
    original_broadcast_date = Column(Date)
    date_added = Column(DateTime, default=datetime.utcnow)
    file_url = Column(String(255))  # URL or path to audio file
    playlist = Column(Text)  # Could be JSON or plain text
    show_type = Column(String(100))
