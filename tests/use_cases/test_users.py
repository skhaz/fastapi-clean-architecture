from app.dtos.user import UserRequest
from app.repositories.memory import MemoryRepository
from app.use_cases.users import UserAddUseCase


def test_user_add_use_case():
    repo = MemoryRepository()
    case = UserAddUseCase(repo)
    user = UserRequest(
        name="test",
        email="me@test.com",
        avatar="https://s3.amazon.com/avatar.jpg",
    )

    data = case.execute(user).dict()

    assert data["name"] == user.name
    assert data["email"] == user.email
    assert data["avatar"] == user.avatar
