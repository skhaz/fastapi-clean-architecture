from dataclasses import dataclass
from typing import Optional
from typing import TypedDict

from app.entities import BaseEntity


class User(TypedDict):
    id: Optional[str]
    name: str
    email: str
    avatar: str


@dataclass
class UserEntity(BaseEntity):
    id: Optional[str]
    name: str
    email: str
    avatar: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
            name=other["name"],
            email=other["email"],
            avatar=other["avatar"],
        )

    @classmethod
    def dict(self) -> User:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar,
        }
