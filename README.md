
python -m venv venv

source venv/bin/activate

pip install poetry

poetry init

poetry add fastapi "uvicorn[standard]" pydantic email-validator

poetry add -G dev black isort flake8 mypy pytest pytest-cov

http://localhost:3000/docs