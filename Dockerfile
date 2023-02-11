FROM python:3.10-slim AS base
ENV PATH /opt/venv/bin:$PATH
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS builder
WORKDIR /opt
RUN python -m venv venv
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root --only main

FROM base
WORKDIR /opt
ARG PORT=3000
ENV PORT $PORT
EXPOSE $PORT
ARG options
ENV OPTIONS $options
COPY --from=builder /opt/venv venv
COPY app app
RUN useradd -r user
USER user
CMD exec uvicorn $OPTIONS --host 0.0.0.0 --port $PORT app.main:app
