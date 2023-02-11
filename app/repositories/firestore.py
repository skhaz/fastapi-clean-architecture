from abc import ABC
from typing import Iterable
from typing import Optional

from google.cloud.firestore import CollectionReference

from app.entities import BaseEntity
from app.entities.user import UserEntity
from app.repositories import BaseRepository


class FirestoreRepository(BaseRepository, ABC):
    def __init__(self, collection: CollectionReference) -> None:
        self.collection = collection

    def get(self, id: str) -> Optional[BaseEntity]:
        return self.collection.document(id).get()

    def list(self) -> Iterable[BaseEntity]:
        return [
            UserEntity.from_dict(document.to_dict() | {"id": document.id})
            for document in self.collection.get()
        ]

    def add(self, other: BaseEntity) -> BaseEntity:
        _, reference = self.collection.add(other.dict())
        other.id = reference.id
        return other

    def remove(self, id: str) -> bool:
        self.collection.document(id).delete()
        return True

    def commit(self) -> None:
        ...
