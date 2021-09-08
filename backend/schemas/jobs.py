from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class JobBase(BaseModel):
    name: Optional[str] = None
    adhar: Optional[str] = None
    # adhar_url: Optional[str] = None
    pen: Optional[str] = None
    # description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Job
class JobCreate(JobBase):
    name: str
    adhar: str
    pen: str


# this will be used to format the response to not to have id,owner_id etc
class ShowJob(JobBase):
    name: str
    adhar: str
    # adhar_url: Optional[str]
    pen: str
    date_posted: date
    # description: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
