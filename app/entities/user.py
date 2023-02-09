from dataclasses import dataclass
from typing import TypedDict

from app.entities import BaseEntity


class User(TypedDict):
    id: str
    name: str
    email: str
    avatar: str


@dataclass
class UserEntity(BaseEntity):
    id: str
    name: str
    email: str
    avatar: str

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
            name=other.get("name"),
            email=other.get("email"),
            avatar=other.get("avatar"),
        )

    def dict(self) -> User:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar,
        }
