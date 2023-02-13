from app.dtos.user import UserRequest
from app.repositories.memory import MemoryRepository
from app.use_cases.users import UserAddUseCase


def test_user_add_use_case():
    data = {
        "name": "test",
        "email": "me@test.com",
        "avatar": "https://s3.amazon.com/avatar.jpg",
    }

    repo = MemoryRepository()
    case = UserAddUseCase(repo)
    user = UserRequest(**data)

    result = case.execute(user).to_dict()

    assert len(result) == 4
    assert result["id"] == "1"
    assert result["name"] == data["name"]
    assert result["email"] == data["email"]
    assert result["avatar"] == data["avatar"]
