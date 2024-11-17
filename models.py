from datetime import datetime
from pydantic import BaseModel

class DescriptionResponse(BaseModel):
    description: str
    title: str
    time_scraped: datetime

class DescriptionRequest(BaseModel):
    description: str
    video_type: str