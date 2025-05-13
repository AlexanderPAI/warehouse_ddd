FROM python:3.13-slim AS base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential tree curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==2.0.1
RUN poetry config virtualenvs.create false && poetry install --no-root

FROM base AS proj

COPY . .

CMD ["python3", "-m", "main"]
