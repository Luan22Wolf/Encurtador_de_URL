from pydantic import BaseModel

class URLBase(BaseModel):
    long_url: str

class URLInfo(URLBase):
    short_code: str

class Config:
    orm_mode = True