from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import HttpUrl
from pydantic.dataclasses import dataclass


class UserRequest(BaseModel):
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr
    avatar: HttpUrl


@dataclass
class UserResponse(BaseModel):
    id: Optional[str]
    name: str
    email: str
    avatar: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
