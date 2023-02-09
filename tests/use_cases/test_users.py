from app.repositories.memory import MemoryRepository
from app.use_cases.users import UserAddUseCase


def test_fail():
    repo = MemoryRepository()
    _ = UserAddUseCase(repo)
